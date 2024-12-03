from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    fields = ['username', 'password']
    redirect_authenticated_user = True

    def get_success_url(self):  # redirect after log in
        return reverse_lazy('todo-list')


class CustomRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response


def user_logout(request):
    logout(request)
    return redirect('login')
