from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustumUserCreationForm
from django.contrib.auth.views import LoginView
# Create your views here.

class SignupView(CreateView):
    form_class=CustumUserCreationForm
    template_name = 'registration.html'
    success_url=reverse_lazy('login')

    def form_valid(self, form):
        user=form.save()
        login(self.request,user)
        return super().form_valid(form)
    
    
class Login(LoginView):
    template_name = "login.html"