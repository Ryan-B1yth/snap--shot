from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib import messages
from checkout.models import Order
from .models import Profile
from .forms import ProfileForm


def user_profile(request):
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated!")
        else:
            messages.error(request, 'There seems to be a problem')
    else:
        form = ProfileForm(instance=profile)
    orders = profile.orders.all()

    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, 'profiles/profile.html', context)


def order_history(request, order_no):
    order = get_object_or_404(Order, order_no=order_no)

    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, 'checkout/checkout_success.html', context)
