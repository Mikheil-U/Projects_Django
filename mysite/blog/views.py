from django.contrib.auth import logout
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Post, Comment


class AboutView(TemplateView):
    template_name = 'about.html'


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):
    model = Post


class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    model = Post
    fields = ['author', 'title', 'text']


class UpdatePostView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    model = Post
    fields = ['author', 'title', 'text']


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
    context_object_name = 'post'


class DraftListView(LoginRequiredMixin, ListView):
    """
     Lists all draft posts
    """
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post
    template_name = 'blog/post_draft_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('create_date')


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)


@login_required
def add_comment_to_post(request, pk: int):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form})


@login_required
def comment_approve(request, pk: int):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk: int):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)


@login_required
def logout_user(request):
    logout(request)
    return redirect('login')

