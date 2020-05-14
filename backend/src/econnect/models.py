# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.

class User(models.Model):
    name=models.CharField(default='No Name',max_length = 120)
    email=models.EmailField(default='No Email',max_length = 254)
    trainings=[]
    department=models.CharField(default='No Deptartment',max_length = 120)
    
    def join(self,tar_train):
        if tar_train is Training:
            self.trainings.add(tar_train)
            tar_train.enrolled.append(self)
            
    def leave(self,tartrain):
        tartrain.enrolled.remove(self)
        self.trainings.remove(tartrain)
        
    def __str__(self):
        return self.name

class Trainer(models.Model):
    name=models.CharField(default='No Name',max_length = 120)
    email=models.EmailField(default='No Email',max_length = 254)
  #  ownedTrainings=[]
    department=models.CharField(default='No Deptartment',max_length = 120)
    
    def __str__(self):
        return self.name
            
class Profile(models.Model):
    target_user= models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic=models.ImageField(default='default.jpg',upload_to='uploads') 

class Training(models.Model):
    training_name=models.CharField(max_length=128)
    materials=models.FileField(upload_to='uploads')
    trainer=models.CharField(max_length=128)
    next_session=models.DateTimeField(max_length=128)
    trainer=models.OneToOneField(Trainer,on_delete=models.CASCADE)                
    enrolled=[] #list of users enrolled in

    def __str__(self):
        return '%s' % (self.training_name)
