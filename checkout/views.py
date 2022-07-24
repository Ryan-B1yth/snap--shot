""" Imports """
import json

import stripe

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

from basket.contexts import basket_contents

from products.models import Product

from profiles.models import Profile
from profiles.forms import ProfileForm

from .forms import OrderForm
from .models import Order, OrderLineItem

import os
if os.path.isfile('env.py'):
    import env


@require_POST
def cache_checkout_data(request):
    """ Cache checkout data """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')
        stripe.PaymentIntent.modify(pid, metadata={
            'basket': json.dumps(request.session.get('basket', {})),
            'save_location': request.POST.get('save_location'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as ex:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=ex, status=400)


def checkout(request):
    """ Checkout view """
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
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_basket = json.dumps(basket)
            order.save()
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
                        for size, quantity in item_data[
                                'items_by_size'].items():
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

            request.session['save_location'] = 'save_location' in request.POST
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

        if request.user.is_authenticated:
            try:
                profile = Profile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'address_1': profile.default_address_1,
                    'address_2': profile.default_address_2,
                    'city': profile.default_city,
                    'country': profile.default_country,
                    'county': profile.default_county,
                    'postcode': profile.default_postcode,
                })
            except Profile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

    return render(request, 'checkout/checkout.html', context)


def checkout_success(request, order_no):
    """ Checkout success view """
    save_location = request.session.get('save_location')
    order = get_object_or_404(Order, order_no=order_no)

    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

        if save_location:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_city': order.city,
                'default_address_1': order.address_1,
                'default_address_2': order.address_2,
                'default_county': order.county,
            }
            user_profile_form = ProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

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
