from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def homeView(request):
    context ={
    
    }
    templete=loader.get_template('home.html')
    return HttpResponse(templete.render(context,request))