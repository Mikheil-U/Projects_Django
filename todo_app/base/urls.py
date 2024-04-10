from django.urls import path
from . import views

urlpatterns = [

    path('', views.TodoListView.as_view(), name='todo-list'),

    path('create-todo/', views.CreateTodo.as_view(), name='create-todo'),
    path('details-todo/<int:pk>/', views.TodoDetailView.as_view(), name='details-todo'),
    path('update-todo/<int:pk>/', views.TodoUpdateView.as_view(), name='update-todo'),
    path('delete-todo/<int:pk>/', views.TodoDeleteView.as_view(), name='delete-todo'),
    path('complete-todo/<int:pk>/', views.complete_task, name='complete-todo'),

]