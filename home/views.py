""" Imports """
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Testimony
from .forms import TestimonyForm


def index(request):
    """ Render home page """
    testimonies = Testimony.objects.all()

    context = {
        'testimonies': testimonies,
    }

    return render(request, 'home/index.html', context)


def create_testimony(request):
    """ Create a testimony """
    form = TestimonyForm(
        request.POST or None,
        initial={
            'user': request.user
        }
    )

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Testimony published, thank you!')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Something went wrong. Please try again.')

    context = {
        'form': form,
    }

    return render(request, 'home/testimonies.html', context)
