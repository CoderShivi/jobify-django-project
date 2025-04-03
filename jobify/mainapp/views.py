from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView,TemplateView
from .models import *
from .forms import ApplicationForm
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
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
class ApplicationView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Applications
    form_class = ApplicationForm
    template_name = "application.html"
    success_url = reverse_lazy("applysuccess")
    success_message = "Application submitted successfully!"

    def get_context_data(self, **kwargs):
        """Pass job details to the template for the form action."""
        context = super().get_context_data(**kwargs)
        context['job'] = get_object_or_404(Jobs, id=self.kwargs['job_id'])
        return context
    
    # def get_form_kwargs(self):
    #     """ Pass the logged-in user to the form. """
    #     kwargs = super().get_form_kwargs()
    #     kwargs["user"] = self.request.user  # Pass the user instance
    #     return kwargs

    def get_initial(self):
        """ Pre-fill the name field with the logged-in user's full name. """
        initial = super().get_initial()
        initial["name"] =  self.request.user 
        initial["email"] = self.request.user.email
        return initial

    def form_valid(self, form):
        job = get_object_or_404(Jobs, id=self.kwargs["job_id"])
        form.instance.name = self.request.user  # Assign logged-in user
        form.instance.job = job  # Assign the job
        return super().form_valid(form)
    
    
class ApplicationSuccessView(TemplateView):
    template_name='success.html'    

# Views for adding, editing and deleting Jobs CRUD
# Create Jobs 
class AddJobs(LoginRequiredMixin , CreateView):
    model=Jobs
    fields=['title','location', 'vacancies','jd','skills','close_date','salary','jobType','salary_based_on']
    template_name='addJobs.html'
    success_url=reverse_lazy('home')
    login_url='login'

# Read - Show job detail
class JobDetails(LoginRequiredMixin, DetailView):
    model=Jobs
    template_name='job_detail.html'
    context_object_name='job'
    login_url = 'login'

    
    

#Update ->

class EditJobs(UpdateView):
    model=Jobs
    fields='__all__'
    template_name='edit_jobs.html'

    def get_success_url(self):
        return reverse('jobdetail',kwargs={'pk':self.object.pk})


# Delete Jobs

class DeleteJobs(DeleteView):
    model=Jobs
    template_name='deletejobs.html'
    success_url=reverse_lazy('home')

# Show application
class showApplicants(ListView):
    model=Applications
    template_name='show_applicants.html'
    context_object_name='applicants'

    def get_queryset(self):
        """Filter applications for the specific job."""
        job_id = self.kwargs['job_id']
        job = get_object_or_404(Jobs, id=job_id)
        return Applications.objects.filter(job=job)
    
    def get_context_data(self, **kwargs):
        """Pass job details to the template."""
        context = super().get_context_data(**kwargs)
        context['job'] = get_object_or_404(Jobs, id=self.kwargs['job_id'])
        return context