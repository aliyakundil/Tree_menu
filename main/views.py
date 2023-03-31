from django.shortcuts import render
from . models import *


def index(request):
    context = Menu.objects.all()
    return render(request, 'main/index.html', {'context':context})
