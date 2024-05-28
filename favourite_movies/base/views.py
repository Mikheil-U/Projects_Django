from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView, CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Playlist, Movie


class PlaylistCreateView(CreateView):
    model = Playlist
    fields = ['title']
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PlaylistsListView(ListView):
    model = Playlist
    template_name = 'base/base.html'
    context_object_name = 'playlists'


class PlayListDetailView(DetailView):
    model = Playlist
    template_name = 'base/playlist_detail.html'
    context_object_name = 'playlist'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        playlist = self.get_object()
        context['movies'] = playlist.movies.all()  # Add movies to the context
        return context


class PlaylistDeleteView(DeleteView):
    model = Playlist
    success_url = '/'


class PlaylistUpdateView(UpdateView):
    model = Playlist
    success_url = '/'
    fields = ['title']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MovieCreteView(CreateView):
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


class MovieListView(ListView):
    model = Movie
    context_object_name = 'movies'
    template_name = 'base/movie_list.html'

    def get_queryset(self):
        playlist_id = self.kwargs.get('playlist_id')
        if playlist_id:
            return Movie.objects.filter(playlists__id=playlist_id)
        return Movie.objects.all()


class MovieDetailView(DetailView):
    model = Movie
    context_object_name = 'movie'
    template_name = 'base/movie_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['playlist_id'] = self.kwargs.get('playlist_id')
        return context


class MovieUpdateView(UpdateView):
    model = Movie
    fields = ['title', 'description', 'genre', 'director', 'release_year', 'imdb_rating']

    def get_success_url(self):
        playlist_id = self.kwargs['playlist_id']
        return reverse_lazy('playlist-details', kwargs={'pk': playlist_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['playlist_id'] = self.kwargs.get('playlist_id')
        return context
