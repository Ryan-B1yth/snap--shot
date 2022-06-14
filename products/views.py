from django.shortcuts import render
from .models import Product
# Create your views here.

def all_products(request):
    """ All products view, product search handling """

    products = Product.objects.all()
    context = {
        'products': products
    }

    return render(request, 'products/products.html', context)
