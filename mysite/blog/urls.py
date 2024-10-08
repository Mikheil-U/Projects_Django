from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('post-detail/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post-create/', views.CreatePostView.as_view(), name='post_create'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('post-update/<int:pk>/', views.UpdatePostView.as_view(), name='post_update'),
    path('post-delete/<int:pk>/', views.DeletePostView.as_view(), name='post_delete'),

    path('drafts/', views.DraftListView.as_view(), name='drafts'),

    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),

    path('logout-user/', views.logout_user, name='logout'),
]
