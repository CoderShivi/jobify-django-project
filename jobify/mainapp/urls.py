from django.urls import path
from .views import homeView, ListSkills, ListJobs

urlpatterns = [
    path("", homeView, name='home' ),
    path('skills', ListSkills.as_view(), name="skills_list"),
    path('jobs', ListJobs.as_view(), name='jobs_list')
]