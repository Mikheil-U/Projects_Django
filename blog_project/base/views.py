from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView
)
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


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



def about(request):
    return render(request, 'base/about.html', {'title': 'About'})
