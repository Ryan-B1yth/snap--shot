""" Imports """
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.views.generic import CreateView
from .models import Product, Category, Review
from .forms import ProductForm, ReviewForm


def all_products(request):
    """ All products view, product search handling """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, 'Please enter a search...')
                return redirect(reverse('products'))

            queries = (
                Q(name__icontains=query) | Q(description__icontains=query)
                )
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ Product detail view """

    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.all()
    context = {
        'product': product,
        'reviews': reviews
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add product view """
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, "Product added to basket.")
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'There seems to be a problem. Please try again.'
                )
    else:
        form = ProductForm()
    context = {
        'form': form
    }

    return render(request, 'products/add_product.html', context)


@login_required
def edit_product(request, product_id):
    """ Edit product view """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product information updated.')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Something went wrong. Please try again.')
    form = ProductForm(instance=product)

    context = {
        'form': form,
        'product': product,
    }

    return render(request, 'products/edit_product.html', context)


@login_required
def delete_product(request, product_id):
    """ Delete product view """
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted.')

    return redirect('products')


@login_required
def review(request, product_id):
    """ Review product """
    default_user = request.user
    product = get_object_or_404(Product, pk=product_id)
    form = ReviewForm(
            request.POST or None,
            initial={
                'user': default_user,
                'product': product
            }
        )
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Review posted.')
            return redirect(reverse('product_detail', args=[product_id]))
        else:
            messages.error(request, 'Something went wrong. Please try again.')

    context = {
        'form': form,
        'product': product
    }

    return render(request, 'products/review.html', context)
