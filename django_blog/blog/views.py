from django.shortcuts import render


def index(request):
    return render(request, 'blog/home.html', {})


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

