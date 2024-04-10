from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    DeleteView,
    UpdateView,
)

from .models import Todo


class TodoListView(LoginRequiredMixin, ListView):
    model = Todo
    template_name = 'base/todo_list.html'
    context_object_name = 'todo_list'

    def get_queryset(self, *args, **kwargs):
        return Todo.objects.filter(user=self.request.user).order_by('completed')  # user specific data


class CreateTodo(LoginRequiredMixin, CreateView):
    model = Todo
    template_name = 'base/todo_create.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('todo-list')

    def form_valid(self, form):
        form.instance.user = self.request.user  # Assign todos to currently logged users.
        return super().form_valid(form)


class TodoDetailView(LoginRequiredMixin, DetailView):
    model = Todo
    template_name = 'base/detail_todo.html'
    context_object_name = 'todo'


class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = Todo
    template_name = 'base/todo_confirm_delete.html'
    success_url = reverse_lazy('todo-list')


class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    fields = ['title', 'description', 'completed']
    template_name = 'base/todo_create.html'
    success_url = reverse_lazy('todo-list')


@require_POST
def complete_task(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.completed = True
    todo.save()
    return redirect('todo-list')
