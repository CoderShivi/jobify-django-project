from django import forms
from .models import Applications
from django.contrib.auth.models import User

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Applications
        fields = [ 'email', 'phone', 'resume', 'cover_letter']
        
        widgets = {  
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

    # def __init__(self, *args, **kwargs):
    #     user = kwargs.pop("user", None)  # Get the user from CBV
    #     super().__init__(*args, **kwargs)
        
    #     if user:
    #         self.fields["name"].queryset = User.objects.filter(id=user.id)  #  Allow only the logged-in user
    #         self.fields["name"].initial = user  # Pre-fill with logged-in user
    #         self.fields["name"].widget = forms.HiddenInput()  #  Hide name field
