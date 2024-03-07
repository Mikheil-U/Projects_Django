from django.shortcuts import render
from .models import Category, Product


def store(request):
    return render(request, 'store/store.html', {'all_products': Product.objects.all()})


def categories(request):

    return {'all_categories': Category.objects.all()}
