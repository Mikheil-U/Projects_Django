from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


def home(request):
    return render(request, 'base/home.html', {'posts': Post.objects.all()})


class PostListView(ListView):
    model = Post
    template_name = 'base/home.html'
    context_object_name = 'posts'  # same as {'posts': Post.objects.all()}
    # ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'base/user_profile.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # UserPassesTestMixin -> Only the authors of the post can update their post
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        # Only the authors of the post can update their post
        post = self.get_object()  # get the post we are currently trying to update
        if self.request.user == post.author:  # make sure the current user is the author of the post
            return True
        return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'  # send to home page

    def test_func(self):
        # Only the authors of the post can update their post
        post = self.get_object()  # get the post we are currently trying to update
        if self.request.user == post.author:  # make sure the current user is the author of the post
            return True
        return False


def about(request):
    return render(request, 'base/about.html', {'title': 'About'})
