from django.shortcuts import render
from .models import Category, Product
from django.shortcuts import get_object_or_404


def store(request):
    return render(request, 'store/store.html', {'all_products': Product.objects.all()})


def categories(request):

    return {'all_categories': Category.objects.all()}


def product_info(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    return render(request, 'store/product-info.html', {'product': product})


def list_category(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/list-category.html', {'category': category, 'products': products})


