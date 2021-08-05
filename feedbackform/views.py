
from .models import Feedback
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render, redirect

def createResponse(request):
     if request.method == 'POST':
          if request.POST.get('name'):
               post=Feedback()
               post.name= request.POST.get('name')
               post.age= request.POST.get('age')
               post.gender= request.POST.get('gender')
               post.save()
                
               #return redirect('home') 
          
               #messages.success(request, f'Your account has been created! You are now able to log in')
               #return redirect('/home')
               #return reverse('home')
               #def get_absolute_url(self):
                    #return u'/some_url/%d' % self.id

          else:
               return render(request,'feedback_form.html')
     def get_absolute_url(self):
          return reverse('home')
class CreateResponse(CreateView):
	model = Feedback
	fields=['name', 'age', 'gender', 'rate_the_session', 'was_the_session_insightful', 'what_is_this', 'name_one_animal', 'question3', 'question4', 'question5']
	template_name = "feedback_form.html"
    

