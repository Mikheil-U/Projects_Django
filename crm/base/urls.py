from django.urls import path
from . import views

urlpatterns = [
    path('', views.PeopleListView.as_view(), name='home'),
    path('add-record/', views.PeopleCreateView.as_view(), name='add-record'),
    path('update-record/<int:pk>', views.PeopleDetailView.as_view(), name='details-record'),
    path('details-record/<int:pk>', views.PeopleUpdateView.as_view(), name='update-record'),
    path('delete-record/<int:pk>', views.PeopleDeleteView.as_view(), name='delete-record'),
]