from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import *
# Create your views here.

def homeView(request):
    context ={
    
    }
    templete=loader.get_template('home.html')
    return HttpResponse(templete.render(context,request))


class ListSkills(ListView):
    model = Skills
    template_name  = 'skills.html'


class ListJobs(ListView):
    model = Jobs
    template_name = 'jobs.html'

