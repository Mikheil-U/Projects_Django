"""
URL configuration for blog_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
# from blog_project.users import views as user_views  # ** NOT WORKING RESEARCH THIS **

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    # path('register', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html',
                                                redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html',
                                                  next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),

    path('', include('users.urls')),
]
