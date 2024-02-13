from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


def home(request):
    return render(request, 'base/home.html', {'posts': Post.objects.all()})


class PostListView(ListView):
    model = Post
    template_name = 'base/home.html'
    context_object_name = 'posts'  # same as {'posts': Post.objects.all()}
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


def about(request):
    return render(request, 'base/about.html', {'title': 'About'})
