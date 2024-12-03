from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.CustomRegisterView.as_view(), name='register'),
]