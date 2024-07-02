from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('', views.RecordListView.as_view(), name='home'),
    path('add-record/', views.RecordCreateView.as_view(), name='add-record'),
    path('update-record/<int:pk>', views.RecordDetailView.as_view(), name='details-record'),
    path('details-record/<int:pk>', views.RecordUpdateView.as_view(), name='update-record'),
    path('delete-record/<int:pk>', views.RecordDeleteView.as_view(), name='delete-record'),
]