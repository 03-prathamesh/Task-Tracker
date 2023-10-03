from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class UserSignUpForm(UserCreationForm):
    class Meta:
      model=User
      fields=['first_name','last_name','email','username']  

class UserLoginForm(AuthenticationForm):
    class Meta:
        model=User
       
        