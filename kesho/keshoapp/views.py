from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'keshoapp/index.html')

def home(request):
    return render(request, 'keshoapp/home.html')

def about(request):
    return render(request, 'keshoapp/about.html')

def jumper(request):
    return render(request, 'keshoapp/jumper.html')

def babe(request):
    return render(request, 'keshoapp/babe.html')

def base(request):
    return render(request, 'keshoapp/base.html')
#trying to add a babe form



def addbabe(request):
    # addedbabe = Babe.objects.get(id = pk)
    getbabeform = AddbabeForm()
    return render(request, 'keshoapp/babe.html', {'getbabeform': getbabeform})
    # babes_form = AddbabeForm(request.POST)
    # if request.method == 'POST':
    #     if babes_form.is_valid():
    #         new_babe = babes_form.save()
    #         # new_babe.save()
    # return render(request, 'keshoapp/babe.html', {'babes_form': babes_form})

