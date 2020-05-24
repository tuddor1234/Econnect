# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.core.urlresolvers import  reverse


import datetime

# Create your models here.


        
    
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()




class Training(models.Model):
    
     training_name=models.CharField(max_length=128)
     description = models.CharField(max_length = 5000, default = "No description has been attached")
    # materials=models.FileField(upload_to='uploads', widget=forms.ClearableFileInput(attrs={'multiple': True}))
    #  img = models.ImageField(True, True)
     
     next_session=models.DateTimeField(max_length=128)
     trainer=models.ForeignKey(User, on_delete=models.CASCADE)                
  #   enrolled=models.ManyToManyField() #list of users enrolled in

     def __str__(self):
        return '%s' % (self.training_name)

     def get_absolute_url(self):
        return reverse('training_detail' , args = [self.training_name] )



class Profile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    profile_pic=models.ImageField(default='default.png',upload_to='profile_pics') 
    name=models.CharField(default='No Name',max_length = 120)
    department=models.CharField(default='No Deptartment',max_length = 120)
    isTrainer = models.BooleanField(default = False)


    trainings = models.ManyToManyField(Training)


    def join(self,tar_train):
        if tar_train is Training:
            self.trainings.add(tar_train)
          #  tar_train.enrolled.append(self)
            
    def leave(self,tartrain):
        tartrain.enrolled.remove(self)
        self.trainings.remove(tartrain)


    # def createTraining(self):
    #     self.trainings.create()