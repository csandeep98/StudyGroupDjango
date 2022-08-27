from multiprocessing import context
from django.shortcuts import render


# Create your views here.

rooms = [
    {'id': 1, 'name': "Lets learn Python"},
    {'id': 2, 'name': "Django hustlers!"},
    {'id': 3, 'name': "Lets create Projects and host them on github"},
]


def home(request):
    context = {'rooms': rooms}
    return render(request, 'home.html', context)


def room(request):
    return render(request, 'room.html')
