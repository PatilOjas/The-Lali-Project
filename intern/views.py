from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import DocumentForm,UserUpdateForm,ProfileUpdateForm,EditTask
from django.contrib.auth.models import User
from .models import Tasks
from django.views.generic import UpdateView,CreateView
import csv
from textblob import TextBlob


def home(request):
    return render(request,'intern/base.html')

def fileUpload(request):
    # task=Tasks.objects.filter(intern=request.user).first()
    userTasks=Tasks.objects.filter(intern=request.user)
    files=[]
    for task in userTasks:
        files.append(task)

    if request.method =='POST':
        form = DocumentForm(request.POST, request.FILES)
        key=request.POST.get('key')
        task=userTasks.filter(pk=key).first()
        if form.is_valid():
            task.file=request.FILES['docfile']
            task.save()
            return HttpResponse('<h1>Uploaded</h1>')
    else:

        form=DocumentForm()
        return render(request,'intern/file.html',{'form':form,'files':files})

def profile(request):
    if request.method =='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('home')

    else:        
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)
        context={
            'uform':u_form,
            'pform':p_form
        }
    return render(request,"intern/intern.html",context)

class TaskCreateView(CreateView):
    model=Tasks
    fields=['title','desc','intern']

    def form_valid(self,form):
        # form.instance.intern=self.request.user
        return super().form_valid(form)

def viewTasks(request):
    tasks=Tasks.objects.filter(isComplete=False)
    files=[]
    for task in tasks:
        files.append(task)
    return render(request,'intern/task-view.html',{'files':files})

def editTasks(request,name,pk):
    user=User.objects.filter(username=name).first()
    tasks=Tasks.objects.filter(intern=user)
    task=tasks.filter(pk=pk).first()
    completedTasks=tasks.filter(isComplete=True).count()
    pendingTasks=tasks.count()-completedTasks
    if request.method =='POST':
        form=EditTask(request.POST) 
        if form.is_valid():
            comments=form.cleaned_data.get('comments')
            isComplete=form.cleaned_data.get('isComplete')
            task.comments=comments
            task.isComplete=isComplete
            task.save()
            redirect('view')
    else:
        form=EditTask() 
    return render(request,'intern/admin-task.html',{'task':task,'form':form,'pending':pendingTasks,'complete':completedTasks})

def feedback(request):
    positive=0
    negative=0
    neutral=0
    with open('sentiments.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for sentence in row:
                print(sentence)
                edu=TextBlob(sentence)
                x=edu.sentiment.polarity
                if x<0:
                    print('negative')
                    negative+=1
                elif x==0:
                    print('Neutral')
                    neutral+=1
                elif x>0 and x<=1:
                    print('positive')
                    positive+=1
    print(positive)
    print(negative)
    return render(request,'intern/feedback.html',{'positive':positive,'negative':negative,'neutral':neutral})



# Create your views here.
