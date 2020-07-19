# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect,get_object_or_404

from django.http import  HttpResponse
from econnect.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from econnect.forms import RegisterForm, UpdateProfileForm
from django import forms
from django.forms import DateTimeField
from django.views.generic import DetailView, ListView, UpdateView, CreateView



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




def training_details(request,training_id):

    t = get_object_or_404(Training, pk = training_id)
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

class TrainingDetailView(LoginRequiredMixin, UserPassesTestMixin,DetailView):
    model = Training
 #   template_name = 'training_detail.html'
 
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
       

def leave(request,tarid):
    
    tar_training = Training.objects.get(pk=tarid)
    request.user.profile.leave(tar_training)
    
    return render(request,'profile.html')

def make_training(request):
    
    if request.method=="POST":
        form = TrainingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard.html")
    
    else:
        form = TrainingForm()
    
    return render(request,'make_training.html',{'tform':form})

def complete(request,tarid):
    tar_training=Training.objects.get(pk=tarid)
    request.user.profile.complete(tar_training)
    
    return render(request,'profile.html')


def editprofile(request):
    if request.method=="POST":
        form=UpdateProfileForm(request.POST,request.FILES,instance=request.user.profile);
        if form.is_valid():
            form.save()
            return redirect("profile.html")
    else: 
        form=UpdateProfileForm(instance=request.user.profile)
    return render(request,'editprofile.html',{'upform':form})

class MakeTrainingView(LoginRequiredMixin, CreateView):
    model=Training
    template_name="make_training.html"
    fields=['training_name','description','department']
    success_url='/dashboard'   
       
    def form_valid(self, form):
        form.instance.trainer = self.request.user
        return super().form_valid(form)


class UpdateTrainingView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model=Training
    fields=['img','next_session','materials','next_session']
    template_name="edittraining.html"
    success_url='/dashboard'
    
    def test_func(self):
        obj = self.get_object()
        return obj.trainer == self.request.user


    def form_valid(self, form):
        form.instance.trainer = self.request.user
        return super().form_valid(form)
    

