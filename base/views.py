from django.shortcuts import render
from django.http import HttpResponse
from .models import Room
# rooms = [

# {'id':1, 'name':'lets run python!'},
# {'id':2, 'name':'Design with me!'},
# {'id':3, 'name':'Frontend developer!'},
# {'id':4, 'name':'django developer!'},
# ]

# Create your views here.
def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i
    context = {'room' : room}
    return render(request,'base/room.html', context)

