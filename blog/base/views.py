from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import PostForm, CommentForm
from .models import Post
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


class AboutView(TemplateView):
    template_name = 'base/about.html'


class PostListView(ListView):
    model = Post
    # template_name = 'base/base.html'
    # context_object_name = 'post'

    def get_queryset(self):
        """
            Used by ListViews - it determines the list of objects that you want to display. By default, it'll just give
            us all for the model you specify. By overriding this method you can extend or completely replace this logic.
        """
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'  # If user is not logged in, redirect here.
    redirect_field_name = 'base/post_detail.html'
    form_class = PostForm
    model = Post


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'  # If user is not logged in, redirect here.
    redirect_field_name = 'base/post_detail.html'
    form_class = PostForm
    model = Post


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post-list')  # redirect after post is deleted


class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'base/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')
