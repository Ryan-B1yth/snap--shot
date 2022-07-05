from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, 'Nothing in the basket')
        return redirect(reverse('products'))
    
    order_form = OrderForm()

    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IQV5IEl9zAfsjE63w7v6gyHVgLuxqRhieQIxStB3TF5EVKsm1ns9ofNHGh8E4OfHcCMqZxfZhk2gOKv5YvUQEvj00SUn4dkGb',
    }

    return render(request, 'checkout/checkout.html', context)