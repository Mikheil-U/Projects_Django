from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
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
        return reverse_lazy('home')


class CustomRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'base/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response


class RecordListView(LoginRequiredMixin, ListView):
    model = Record
    context_object_name = 'records'
    template_name = 'base/base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['records'] = context['records'].filter(user=self.request.user)

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['records'] = context['records'].filter(name__icontains=search_input)
        context['search_input'] = search_input
        return context


class RecordDetailView(LoginRequiredMixin, DetailView):
    model = Record
    context_object_name = 'record'
    template_name = 'base/record-detail.html'


class RecordCreateView(LoginRequiredMixin, CreateView):
    model = Record
    template_name = 'base/add-record.html'
    fields = ['name', 'address', 'city', 'state', 'zip']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class RecordUpdateView(LoginRequiredMixin, UpdateView):
    model = Record
    fields = ['name', 'address', 'city', 'state', 'zip']
    template_name = 'base/add-record.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class RecordDeleteView(LoginRequiredMixin, DeleteView):
    model = Record
    success_url = reverse_lazy('home')


@login_required()
def user_logout(request):
    logout(request)
    return redirect('login')
