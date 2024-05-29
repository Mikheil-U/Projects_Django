from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
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
        return context


class PlayListDetailView(LoginRequiredMixin, DetailView):
    model = Playlist
    template_name = 'base/playlist_detail.html'
    context_object_name = 'playlist'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        playlist = self.get_object()
        context['movies'] = playlist.movies.all()  # Add movies to the context
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


# class MovieListView(ListView):
#     model = Movie
#     context_object_name = 'movies'
#     template_name = 'base/movie_list.html'
#
#     def get_queryset(self):
#         playlist_id = self.kwargs.get('playlist_id')
#         if playlist_id:
#             return Movie.objects.filter(playlists__id=playlist_id)
#         return Movie.objects.all()


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
