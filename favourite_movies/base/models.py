from django.db import models
from django.contrib.auth.models import User


class Playlist(models.Model):
    title = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movies = models.ManyToManyField('Movie', related_name='playlists')

    def __str__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    genre = models.CharField(max_length=250, blank=True, null=True)
    director = models.CharField(max_length=250, blank=True, null=True)
    release_year = models.DateTimeField(null=True, blank=True)
    imdb_rating = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


