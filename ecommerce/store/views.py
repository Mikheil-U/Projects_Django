from django.shortcuts import render
from .models import Category, Product
from django.shortcuts import get_object_or_404


def store(request):
    return render(request, 'store/store.html', {'all_products': Product.objects.all()})


def categories(request):

    return {'all_categories': Category.objects.all()}


def product_info(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/product-info.html', {'product': product})
