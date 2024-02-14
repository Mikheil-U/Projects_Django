from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.views.generic.list import ListView
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.detail import DetailView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Movie


class CustomLogin(LoginView):
    model = Movie
    template_name = 'base/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('movies-list')


class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm  # Set the form
    redirect_authenticated_user = True
    success_url = reverse_lazy('movies-list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        """ If users are already logged in, restrict the register page and redirect to home page."""
        if self.request.user.is_authenticated:
            return redirect('movies-list')
        return super(RegisterPage, self).get(*args, **kwargs)


class MoviesList(LoginRequiredMixin, ListView):
    model = Movie
    template_name = 'base/movies_list.html'
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        """ For user specific data, so the user only gets their own data. """
        context = super().get_context_data(**kwargs)
        context['movies'] = context['movies'].filter(user=self.request.user)
        return context


def custom_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully")
    return redirect('login')


class AddMovie(LoginRequiredMixin, CreateView):
    model = Movie
    fields = ['title', 'release_year', 'genre', 'director', 'imdb_rating']
    success_url = reverse_lazy('movies-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddMovie, self).form_valid(form)


class MovieDetail(LoginRequiredMixin, DetailView):
    model = Movie
    template_name = 'base/movie_detail.html'
    context_object_name = 'movie'


class MovieDelete(LoginRequiredMixin, DeleteView):
    model = Movie
    context_object_name = 'movie'
    success_url = reverse_lazy('movies-list')


class UpdateMovie(UpdateView):
    model = Movie
    fields = ['title', 'release_year', 'genre', 'director', 'imdb_rating']
    success_url = reverse_lazy('movies-list')






