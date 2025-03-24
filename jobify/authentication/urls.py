from django.urls import path
from .views import SignupView, Login

urlpatterns = [
    path('signup/', SignupView.as_view(), name='register'),
    path('login/', Login.as_view(), name='login')
]