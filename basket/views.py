from django.shortcuts import render, redirect, reverse, HttpResponse


def basket_view(request):
    """ Basket view """
    return render(request, 'basket/basket.html', {})


def add_to_basket(request, product_id):
    """ Add quantities to basket """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    basket = request.session.get('basket', {})

    if size:
        if product_id in list(basket.keys()):
            if size in basket[product_id]['items_by_size'].keys():
                basket[product_id]['items_by_size'][size] += quantity
            else:
                basket[product_id]['items_by_size'][size] = quantity
        else:
            basket[product_id] = {'items_by_size': {size: quantity}}
    else:
        if product_id in list(basket.keys()):
            basket[product_id] += quantity
        else:
            basket[product_id] = quantity

    request.session['basket'] = basket

    return redirect(redirect_url)


def update_basket(request, product_id):
    """ Update quantities in basket """
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    basket = request.session.get('basket', {})

    if size:
        if quantity > 0:
            basket[product_id]['item_by_size'][size] = quantity
        else:
            del basket[product_id]['item_by_size'][size]
            if not basket[product_id]['item_by_size']:
                basket.pop(product_id) 
    else:
        if quantity > 0:
            basket[product_id] = quantity
        else:
            basket.pop(product_id)

    request.session['basket'] = basket

    return redirect(reverse('basket'))


def remove_item(request, product_id):
    """ Remove item from basket """
    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        basket = request.session.get('basket', {})

        if size:
            del basket[product_id]['items_by_size'][size]
            if not basket[product_id]['items_by_size']:
                basket.pop(product_id)
        else:
            basket.pop(product_id)

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception:
        return HttpResponse(status=500)
