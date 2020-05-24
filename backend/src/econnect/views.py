# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect,get_object_or_404

from django.http import  HttpResponse
from models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from forms import RegisterForm

from django.views.generic import DetailView, ListView



# Create your views here.

def home(request):
    return redirect("profile")

@login_required
def profile(request):

    myTrainings = request.user.profile.trainings.all()
    return render(request,'profile.html', {'myTrainings': myTrainings})

@login_required
def dashboard(request):

    trainings = Training.objects.all()

    context = {
        "trainings" : trainings
    }

    return render(request,'dashboard.html', context)

@login_required
def enroll(request,tarid):

    enrolledTraining = Training.objects.get(pk=tarid)
    request.user.profile.join(enrolledTraining)

    trainings = Training.objects.all()
    

    context = {
        "trainings" : trainings
    }

    return render(request,'dashboard.html', context)




def training_details(request, training_name):

    t = get_object_or_404(Training, training_name = training_name)
    context = {'training' : t}
    return render(request,'training_detail.html', context)



def register(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid(): 
            user = form.save()
            user.refresh_from_db()
            user.profile.name = form.cleaned_data['name']
            user.profile.department = form.cleaned_data['department']

            user.save()

            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect("profile")
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




class TrainingListView(ListView):
    model = Training
    template_name = 'dashboard.html'
    context_object_name = 'trainings' 
    ordering = ['-next_session']

 
class TrainingDetailView(DetailView):
    model = Training
 #   template_name = 'training_detail.html'
       

def leave(request,tarid):
    
    tar_training = Training.objects.get(pk=tarid)
    request.user.profile.leave(tar_training)
    
    return render(request,'profile.html')

def make_training(request):
    
    if request.method=="POST":
        form=TrainingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("profile")
    
    else:
        form=TrainingForm()
    
    return render(request,'make_training.html',{'tform':form})

