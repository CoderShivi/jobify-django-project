# applications/forms.py
from django import forms
from .models import Applications

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Applications
        fields = ['name', 'email', 'phone', 'resume', 'cover_letter']
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your full name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email address',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your phone number',
            }),
            'resume': forms.ClearableFileInput(attrs={
                'class': 'form-control-file',
            }),
            'cover_letter': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Write your cover letter here...',
            }),
        }
