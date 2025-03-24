from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView,TemplateView
from .models import *
from .forms import ApplicationForm
from django.urls import reverse_lazy
# Create your views here.

def homeView(request):
    jobs_list=Jobs.objects.all()
    context={
        'jobs_list':jobs_list
    }
    templete=loader.get_template('home.html')
    return HttpResponse(templete.render(context,request))


class ListSkills(ListView):
    model = Skills
    template_name  = 'skills.html'
    


class ListJobs(ListView):
    model = Jobs
    template_name = 'jobs.html'

# Create Application 
class ApplicationView(SuccessMessageMixin,CreateView):
    model=Applications
    form_class=ApplicationForm
    template_name='application.html'
    success_url=reverse_lazy('application.html')
    success_message="Application submitted successfully!"

    def form_valid(self, form):
        return super().form_valid(form)

class ApplicationSuccessView(TemplateView):
    template_name='success.html'    

# Views for adding, editing and deleting Jobs CRUD
# Create Jobs 
class AddJobs(CreateView):
    model=Jobs
    fields=['title','vacancies','jd','skills','close_date','salary','jobType','salary_based_on']
    template_name='addJobs.html'
    success_url=reverse_lazy('home')
