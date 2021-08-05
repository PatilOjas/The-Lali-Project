from django.shortcuts import render
from datetime import datetime
from .models import Link
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)


from django.views.generic import (TemplateView , DetailView ,ListView,FormView,CreateView,UpdateView,DeleteView)

# Create your views here.
def current_meeting(request):
    current_time = datetime.now()

    current_hour = current_time.hour #3:00 pm -> 15
    current_min = current_time.minute #3:00 pm -> 0

    meeting_list = list(Link.objects.all())

    current_meeting = None

    def time_in_mins(hr, min):
        return hr * 60 + min

    for meeting in meeting_list:
        start_time_hour = meeting.start_time.hour
        start_time_min = meeting.start_time.minute

        end_time_hour = meeting.end_time.hour
        end_time_min = meeting.end_time.minute

        day_list = []

        if meeting.monday == True:
            day_list.append('Monday')
        if meeting.tuesday == True:
            day_list.append('Tuesday')
        if meeting.wednesday == True:
            day_list.append('Wednesday')
        if meeting.thursday == True:
            day_list.append('Thursday')
        if meeting.friday == True:
            day_list.append('Friday')
       

        
        
        current_meeting = meeting
    

    if current_meeting == None:
        return render(request, 'nomeetings.html')

    else:
        return render(request, 'linktoclick.html', {'obj': current_meeting})

from .models import Link
from .forms import AddForm
 
 
def create_view(request):
    context={}
    if request.method=="POST":   
        
    # add the dictionary during initialization
        form = AddForm(request.POST)
        if form.is_valid():
            print('hello')
            form.save()
        context['form']= form
      
    else:
          
        form=AddForm()
        context['form']= form
    return render(request, "create_view.html", context)


    
