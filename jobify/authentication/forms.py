from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class CustumUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm your password'}),
        }
        labels={
            'username':'Username',
            'email':'Email',
            'password1':'Password',
            'password2':'Confirm Password'
        }
        help_texts={
            'username':None,
            'email':None,
            'password1':None,
            'password2':None
        }


# class CustomUserEditForm(UserChangeForm):
#     class Meta:
#         model = User
#         fields = ['username','email']

# class UserEditForm(forms.ModelForm):
#     class Meta:
#         fields = ['username','email']
#         model = User
#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'form-control'}),
#             'email':forms.TextInput(attrs={'class':'form-control'}),
#         }
