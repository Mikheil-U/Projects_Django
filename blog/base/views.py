from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import PostForm, CommentForm
from .models import Post, Comment
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView
)


class AboutView(TemplateView):
    template_name = 'base/about.html'


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'post_list'

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


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post-detail', pk=pk)


@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post  # connect the comment to the post
            comment.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'base/comment_form.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post-detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post-detail', pk=post_pk)
