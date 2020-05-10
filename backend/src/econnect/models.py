# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.


class User:
    def __init__(self,name,email,department,profile_pic):
        self.name=str(name)
        self.email=str(email)
        self.profile_pic=str(profile_pic) #URL FOR PICTURE
        self.trainings=[]
        self.department=str(department)
    def enroll(self,tartrain):
        if tartrain is Training:
            self.trainings.add(tartrain)
    def leave(self,tartrain):
        for tr in self.trainings:
            if tr.tname == tartrain.tname:
                self.trainings.remove(tr)
                break
    

class Trainer(User):
    def __init__(self,name,email,department,profile_pic):
        super().__init__(name, email, department, profile_pic)
        self.trainerat=[]


class Profile:
    def __init__(self,user):
        self.name=user.name
        self.email=user.email
        self.department=user.department
        self.training_list=user.trainings
        
        
class Training:
    def __init__(self,name,tra):
        self.tname=str(name)
        self.materials=[]
        tra.trainerat.append(self)
        self.trainer=tra
        self.nextsession=datetime()

class Test(models.Model):
    title = models.CharField(max_length = 120);

    def __str__(self):
        return self.title
