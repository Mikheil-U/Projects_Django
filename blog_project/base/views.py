from django.shortcuts import render
from .models import Post


def home(request):
    return render(request, 'base/home.html', {'posts': Post.objects.all()})


def about(request):
    return render(request, 'base/about.html', {'title': 'About'})
