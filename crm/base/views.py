from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Person


class PeopleListView(ListView):
    model = Person
    context_object_name = 'people'
    template_name = 'base/base.html'


class PeopleDetailView(DetailView):
    model = Person
    context_object_name = 'person'
    template_name = 'base/record-detail.html'


class PeopleCreateView(CreateView):
    model = Person
    template_name = 'base/add-record.html'
    fields = ['name', 'address', 'city', 'state', 'zip']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PeopleUpdateView(UpdateView):
    model = Person
    fields = ['name', 'address', 'city', 'state', 'zip']
    template_name = 'base/add-record.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PeopleDeleteView(DeleteView):
    model = Person
    success_url = reverse_lazy('home')
