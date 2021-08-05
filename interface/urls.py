from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.current_meeting, name='current_meeting'),
    path('createmeet/',views.create_view,name='create_view'),
    
]
