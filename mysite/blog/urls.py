from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('post-detail/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post-create/', views.CreatePostView.as_view(), name='post_create'),
    path('post-update/<int:pk>/', views.UpdatePostView.as_view(), name='post_update'),
    path('post-delete/<int:pk>/', views.DeletePostView.as_view(), name='post_delete'),
    path('drafts', views.DraftListView.as_view(), name='drafts'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),

]
