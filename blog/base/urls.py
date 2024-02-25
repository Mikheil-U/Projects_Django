from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post-list'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post-create/', views.PostCreateView.as_view(), name='post-create'),
    path('post-update/<int:pk>/', views.PostUpdateView.as_view(), name='post-update'),
    path('post-delete/<int:pk>/', views.PostDeleteView.as_view(), name='post-delete'),
    path('drafts/', views.DraftListView.as_view(), name='post-draft-list'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='post-add-comment'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='post-comment-approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='post-comment-remove'),
    path('post/<int:pk>/publish/', views.post_publish, name='post-publish'),
]
