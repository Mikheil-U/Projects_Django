from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post-list'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post-create/', views.PostCreateView.as_view(), name='post-create'),
    path('post-update/<int:pk>/', views.PostUpdateView.as_view(), name='post-update')
]
