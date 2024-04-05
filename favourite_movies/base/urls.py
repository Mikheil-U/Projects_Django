from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('', views.MovieListsView.as_view(), name='lists'),

    path('movies/', views.MoviesList.as_view(), name='movies-list'),

    path('login/', views.CustomLogin.as_view(), name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('register/', views.RegisterPage.as_view(), name='register'),

    path('add-movie/', views.AddMovie.as_view(), name='add-movie'),
    path('detail-movie/<int:pk>/', views.MovieDetail.as_view(), name='detail-movie'),
    path('delete-movie/<int:pk>/', views.MovieDelete.as_view(), name='delete-movie'),
    path('update-movie/<int:pk>/', views.UpdateMovie.as_view(), name='update-movie'),
]