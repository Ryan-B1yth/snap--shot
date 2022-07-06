import os
if os.path.isfile('env.py'):
    import env
from django.shortcuts import (
    render,
    reverse,
    redirect,
    get_object_or_404,
    HttpResponse
    )
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from basket.contexts import basket_contents
from products.models import Product
from .models import Order, OrderLineItem

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')
        stripe.PaymentIntent.modify(pid, metadata={
            'basket': json.dumps(request.session.get('basket', {})),
            'save-location': request.POST.get('save-location'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as ex:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=ex, status=400)


def checkout(request):
    stripe_public_key = os.environ.get('STRIPE_PUBLIC_KEY')
    stripe_secret_key = os.environ.get('STRIPE_SECRET_KEY')

    if request.method == 'POST':
        basket = request.session.get('basket', {})
        form_data = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'city': request.POST['city'],
            'address_1': request.POST['address_1'],
            'address_2': request.POST['address_2'],
            'county': request.POST['county'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in basket.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(
                        request,
                        "It seems an item in your basket isn't in our database"
                        "Please get in touch so we can assist you!"
                        )
                    order.delete()
                    return redirect(reverse('products'))
            
            request.session['save-location'] = 'save-location' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_no]))
        else:
            messages.error(
                request,
                "There was a problem with your form."
                "Please try again."
                )
    else:
        basket = request.session.get('basket', {})
        if not basket:
            messages.error(request, 'Nothing in the basket')
            return redirect(reverse('products', args=[order.order_no]))

        current_basket = basket_contents(request)
        total = current_basket['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRNECY
        )
        order_form = OrderForm()

        print(intent)

        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

    return render(request, 'checkout/checkout.html', context)


def checkout_success(request, order_no):
    save_location = request.session.get('save-location')
    order = get_object_or_404(Order, order_no=order_no)
    messages.success(
        request,
        'Order success! Please check your email for a receipt'
        f'{order_no}'
        )
    if 'basket' in request.session:
        del request.session['basket']
    
    context = {
        'order': order,
    }

    return render(request, 'checkout/checkout_success.html', context)