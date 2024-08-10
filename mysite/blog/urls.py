from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('post-detail/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post-create/', views.CreatePostView.as_view(), name='post_create'),
    path('post-update/<int:pk>/', views.UpdatePostView.as_view(), name='post_update'),
]
