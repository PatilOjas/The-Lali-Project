
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
    #path('disp',views.model_form_upload,name='disp'),
    path('', views.Home.as_view(), name='home1'),
    path('books/', views.book_list, name='book_list'),
    path('books/mentor', views.book_list_mentor, name='book_list_mentor'),
    path('books/upload/', views.upload_book, name='upload_book'),
    path('books/<int:pk>/', views.delete_book, name='delete_book'),
    path('books/<int:pk>/', views.grade_book, name='grade_book'),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)