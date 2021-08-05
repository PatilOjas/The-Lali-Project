from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('msg', views.room, name='msg'),
    path('room/<str:room>', views.room, name='chatroom'),
    path('check', views.checkview, name='check'),
    path('send', views.sendmsg, name='sendm'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]