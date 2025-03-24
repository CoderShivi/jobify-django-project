from django.urls import path
from .views import homeView, ListSkills, ListJobs,ApplicationView,ApplicationSuccessView,AddJobs

urlpatterns = [
    path("", homeView, name='home' ),
    path('skills', ListSkills.as_view(), name="skills_list"),
    path('jobs', ListJobs.as_view(), name='jobs'),
    path('apply/',ApplicationView.as_view(),name='apply'),
    path('success',ApplicationSuccessView.as_view(),name='applysuccess'),
    path('jobs/add',AddJobs.as_view(),name='addJob')
]