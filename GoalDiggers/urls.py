"""GoalDiggers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from login import views as user_views
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', user_views.home ,name='home'),
    path('admin/', admin.site.urls,name='admin'),
    path('register/',user_views.register,name='register'),
    path('login/',user_views.login,name='login'),
    path('dboard/',user_views.dboard,name='dashboard'),


    path('chat/', include('chat.urls') ,name='chat'),
    path('meets/',include('interface.urls'),name='interface'),

    path('assign/',include('assignments.urls'),name='assignments'),
    path('mentoring/', include('myapp.urls'),name='mentoring'),
    path('feedbackform/',include('feedbackform.urls'),name='feedbackform'),

]
