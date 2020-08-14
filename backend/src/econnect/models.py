from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import os
#from django.core.urlresolvers import  reverse
from django.urls import reverse

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
     materials=models.FileField(upload_to='resources',null=True,blank=True)
     img = models.ImageField( default = 'static/default_training.jpg'  ,upload_to = 'trainingsPhoto')
     department = models.CharField(max_length=128, default="No department")
  
     next_session=models.DateTimeField(max_length=128, null=True, blank = True)
     trainer=models.ForeignKey(User, on_delete=models.CASCADE)                
     enrolled=[]
     def __str__(self):
        return '%s' % (self.training_name)

     def filename(self):
        return os.path.basename(self.materials.url)

     def get_absolute_url(self):
        return reverse('training_detail' , args = [self.training_name] )

class Profile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    profile_pic=models.ImageField(default='static/default.png',upload_to='profile_pics') 
    name=models.CharField(default='No Name',max_length = 120)
    department=models.CharField(default='No Deptartment',max_length = 120)

    isTrainer = models.BooleanField(default = False)


    trainings = models.ManyToManyField(Training, blank = True)
    completed=[]
    completedtrainings=[]
    
    def __str__(self):
        return self.name

    def complete(self,complet):

        self.trainings.remove(complet.trainingcompleted)
        self.completed.append(complet)
        self.completedtrainings.append(complet.trainingcompleted)

    def join(self,tar_train):
        self.trainings.add(tar_train)
        tar_train.enrolled.append(self)
            
    def leave(self,tartrain):
        tartrain.enrolled.remove(self)
        self.trainings.remove(tartrain)

    def createTraining(self):
        self.trainings.object

     

class Completion(models.Model):
	
	trainingcompleted=models.OneToOneField(Training,on_delete=models.DO_NOTHING)
	datecompleted=models.DateTimeField()

