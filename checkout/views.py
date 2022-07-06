import os
if os.path.isfile('env.py'):
    import env
from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from basket.contexts import basket_contents

import stripe


def checkout(request):
    stripe_public_key = os.environ.get('STRIPE_PUBLIC_KEY')
    stripe_secret_key = os.environ.get('STRIPE_SECRET_KEY')
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, 'Nothing in the basket')
        return redirect(reverse('products'))

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
