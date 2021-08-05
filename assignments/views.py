
from django.shortcuts import render, redirect, render
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
#from GoalDiggers.login.models import NewUser
from .forms import BookForm
from .models import Assignments
from django.apps import apps
MyModel1 = apps.get_model('login', 'NewUser')

class Home(TemplateView):
    template_name = 'home1.html'

def book_list(request):
    books = Assignments.objects.all()
    
    #print(books)
    return render(request, 'book_list.html', {'books': books} )


def book_list(request):
    books = Assignments.objects.all()
    return render(request, 'book_list.html', {'books': books} )



def book_list_mentor(request):
    books = Assignments.objects.all()
    return render(request, 'book_list_mentor.html', {'books': books} )

def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'upload_book.html', {
        'form': form
    })


def delete_book(request, pk):
    if request.method == 'POST':
        book = Assignments.objects.get(pk=pk)
        book.delete()
    return redirect('book_list')


def grade_book(request, pk):
    if request.method == 'POST':
        m=request.POST["mark"]
        book = Assignments.objects.filter(pk=pk)
        book.update(marks=m)
    return redirect('book_list_mentor')
