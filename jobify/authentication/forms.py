from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustumUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm your password'}),
        }
        labels={
            'username':'Username',
            'password1':'Password',
            'password2':'Confirm Password'
        }
        help_texts={
            'username':None,
            'password1':None,
            'password2':None
        }