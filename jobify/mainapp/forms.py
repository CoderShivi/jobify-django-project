from django import forms

from .models import Jobs, Skills

class JobForm(forms.ModelForm):
    skills = forms.MultipleChoiceField(Skills.objects.all())