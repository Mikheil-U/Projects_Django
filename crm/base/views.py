from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Record


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('playlists')


class PeopleListView(ListView):
    model = Record
    context_object_name = 'record'
    template_name = 'base/base.html'


class PeopleDetailView(DetailView):
    model = Record
    context_object_name = 'record'
    template_name = 'base/record-detail.html'


class PeopleCreateView(CreateView):
    model = Record
    template_name = 'base/add-record.html'
    fields = ['name', 'address', 'city', 'state', 'zip']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PeopleUpdateView(UpdateView):
    model = Record
    fields = ['name', 'address', 'city', 'state', 'zip']
    template_name = 'base/add-record.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PeopleDeleteView(DeleteView):
    model = Record
    success_url = reverse_lazy('home')


def user_logout(request):
    logout(request)
    return redirect('login')
