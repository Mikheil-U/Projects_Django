from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    # Authentication
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.CustomRegisterView.as_view(), name='register'),

    # Playlists
    path('', views. PlaylistsListView.as_view(), name='playlists'),
    path('playlist/create/', views.PlaylistCreateView.as_view(), name='playlist-create'),
    path('playlist/<int:pk>/', views. PlayListDetailView.as_view(), name='playlist-details'),
    path('playlist/delete/<int:pk>/', views. PlaylistDeleteView.as_view(), name='playlist-delete'),
    path('playlist/update/<int:pk>/', views. PlaylistUpdateView.as_view(), name='playlist-update'),

    # Movies
    path('movie/watched/<int:pk>/', views.MarkWatchedMovie.as_view(), name='movie-watched'),

    path('movie/<int:pk>/<int:playlist_id>/', views. MovieDetailView.as_view(), name='movie-detail'),
    path('movie/add/<int:playlist_id>/', views. MovieCreteView.as_view(), name='movie-create'),
    path('movie/update/<int:playlist_id>/<int:pk>/', views. MovieUpdateView.as_view(), name='movie-update'),
    path('movie/delete/<int:playlist_id>/<int:pk>/', views. MovieDeleteView.as_view(), name='movie-delete'),



]