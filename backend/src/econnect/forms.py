from django import forms
from django_tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker
from .models import Profile 
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Training, Profile

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    name = forms.CharField(max_length=120)
    profile_pic=forms.ImageField( required=False)
    department = forms.CharField(max_length=120)
    
    # DE ADAUGAT PROFILE PICTURE


    class Meta:
        model = User
        fields = ["username", "name", "department" , "email", "password1" , "password2",]



    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        if commit:
            user.save()
        return user

    
class TrainingForm(forms.ModelForm):

    # training_name = forms.CharField(max_length=120 , label = "Training name")
    # description = forms.CharField(label = "Training description")

    # img = forms.ImageField( label = "Choose a photo for your training" )
    # materials = forms.FileField(label = "Choose materials for your training")

    
    
   
    class Meta:
        model = Training        
        
        fields = [ 
            'training_name',
            'description',
            'department',
            'img',
            #'materials',
            'next_session',  

            'trainer',

            ]
