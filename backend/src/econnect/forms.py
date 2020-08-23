from django import forms
from econnect.models import Profile 
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from econnect.models import Training

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    name = forms.CharField(max_length=120)
    #profile_pic=forms.ImageField( required=False)
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
    
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields = ['name','profile_pic','department']
        
