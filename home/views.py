""" Imports """
from django.shortcuts import render


def index(request):
    """ Render home page """
    return render(request, 'home/index.html', {})
