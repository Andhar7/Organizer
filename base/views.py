from django.http import HttpResponse
from django.shortcuts import render
from .models import Room
from . forms import RoomForm

'''
rooms = [
    {'id': 1, 'name': 'Peace Run News'},
    {'id': 2, 'name': '3100 mile Race'},
    {'id': 3, 'name': 'Looking for a job'},
]
'''


def home(request):
    # return HttpResponse("Welcome to the home page!")
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=int(pk))
    context = {'room': room}
    return render(request, 'base/room.html', context)


def create_room(request):
    form = RoomForm()
    context = {'form': form}
    return render(request, 'base/room_form.html', context)


'''
def room(request, pk):
    # return HttpResponse("Welcome to the room page!")
    room = None
    rooms = Room.objects.all()
    for r in rooms:
        if r['id'] == int(pk):
            room = r
    context = {'room': room}
    return render(request, 'base/room.html', context)

'''
