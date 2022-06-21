from django.shortcuts import render


def basket(request):
    """ Basket view """
    return render(request, 'basket/basket.html', {})
