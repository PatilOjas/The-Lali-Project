from django.shortcuts import render, redirect
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def home(request):
    return render(request, 'home.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    print("hi")
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return HttpResponseRedirect(reverse('chatroom', args=(room,)))
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return HttpResponseRedirect(reverse('chatroom', args=(room,)))

def sendmsg(request):
    print("in msg")
    print(request.POST)
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message(value=message)
    new_message.save()
    return render(request, 'room.html')
    #return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    print("in room")

    messages = Message.objects.all()
    #return render(request,'room.html',{'msgs':messages})
    return JsonResponse({"messages":list(messages.values())})