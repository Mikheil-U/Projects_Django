from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.http import require_POST
from django.views.generic import DeleteView, UpdateView, CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Playlist, Movie


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('playlists')


class CustomRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'base/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')


class PlaylistCreateView(LoginRequiredMixin, CreateView):
    model = Playlist
    fields = ['title']
    success_url = reverse_lazy('playlists')

    def form_valid(self, form):
        """ For user specific data. """
        form.instance.user = self.request.user
        return super().form_valid(form)


class PlaylistsListView(LoginRequiredMixin, ListView):
    model = Playlist
    template_name = 'base/base.html'
    context_object_name = 'playlists'

    def get_context_data(self, **kwargs):
        """ User specific data """
        context = super().get_context_data(**kwargs)
        context['playlists'] = context['playlists'].filter(user=self.request.user)
        context['count'] = context['playlists'].count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['playlists'] = context['playlists'].filter(
                title__icontains=search_input)
        context['search_input'] = search_input
        return context


class PlayListDetailView(LoginRequiredMixin, DetailView):
    model = Playlist
    template_name = 'base/playlist_detail.html'
    context_object_name = 'playlist'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        playlist = self.get_object()
        context['movies'] = playlist.movies.all()  # Add movies to the context
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['movies'] = context['movies'].filter(
                title__icontains=search_input)
        context['search_input'] = search_input
        return context


class PlaylistDeleteView(LoginRequiredMixin, DeleteView):
    model = Playlist
    success_url = reverse_lazy('playlists')


class PlaylistUpdateView(LoginRequiredMixin, UpdateView):
    model = Playlist
    success_url = reverse_lazy('playlists')
    fields = ['title']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MovieCreteView(LoginRequiredMixin, CreateView):
    model = Movie
    fields = ['title', 'description', 'genre', 'director', 'release_year', 'imdb_rating']

    def get_success_url(self):
        playlist_id = self.kwargs['playlist_id']
        return reverse_lazy('playlist-details', kwargs={'pk': playlist_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['playlist_id'] = self.kwargs['playlist_id']
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        playlist_id = self.kwargs['playlist_id']
        playlist = Playlist.objects.get(pk=playlist_id)
        playlist.movies.add(self.object)
        return response


class MovieDetailView(LoginRequiredMixin, DetailView):
    model = Movie
    context_object_name = 'movie'
    template_name = 'base/movie_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['playlist_id'] = self.kwargs.get('playlist_id')
        return context


class MovieUpdateView(LoginRequiredMixin, UpdateView):
    model = Movie
    fields = ['title', 'description', 'genre', 'director', 'release_year', 'imdb_rating']

    def get_success_url(self):
        playlist_id = self.kwargs['playlist_id']
        return reverse_lazy('playlist-details', kwargs={'pk': playlist_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['playlist_id'] = self.kwargs.get('playlist_id')
        return context


class MovieDeleteView(LoginRequiredMixin, DeleteView):
    model = Movie

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['playlist_id'] = self.kwargs.get('playlist_id')
        return context

    def get_success_url(self):
        playlist_id = self.kwargs['playlist_id']
        return reverse_lazy('playlist-details', kwargs={'pk': playlist_id})


@method_decorator(require_POST, name='dispatch')
class ToggleWatchedMovie(View):
    def post(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        movie.watched = not movie.watched
        movie.save()
        return JsonResponse({'success': True, 'watched': movie.watched})

