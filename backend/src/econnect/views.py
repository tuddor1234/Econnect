# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect
from django.http import  HttpResponse
from econnect.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from econnect.forms import RegisterForm


# Create your views here.

def home(request):
    return render(request,'home.html')

@login_required
def profile(request):


    return render(request,'profile.html')

@login_required
def dashboard(request):

    trainings = Training.objects.all()

    context = {
        "trainings" : trainings
    }

    return render(request,'dashboard.html', context)


def enroll(request,tarid):

    enrolledTraining = Training.objects.get(pk=tarid)
    request.user.profile.join(enrolledTraining)

    trainings = Training.objects.all()

    context = {
        "trainings" : trainings
    }

    return render(request,'dashboard.html', context)


def training_details(request):

    # enrolledTraining = Training.objects.get(requ)
    # user.profile.join()

    trainings = Training.objects.all()

    context = {
        "trainings" : trainings
    }

    return render(request,'training_details.html', context)





def register(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()

    # if request.method == "POST":
    #    form = UserCreationForm(request.POST)
    #    if form.is_valid():
    #        form.save()
    #        username = form.cleaned_data.get('username')
    #        return redirect('home')
    # else:
    #     form = UserCreationForm()

    return render(request,"register.html",{"form" : form})
