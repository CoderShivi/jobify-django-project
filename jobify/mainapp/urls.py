from django.urls import path
from .views import homeView, ListSkills, ListJobs,ApplicationView,ApplicationSuccessView,AddJobs,DeleteJobs,JobDetails,EditJobs,showApplicants

urlpatterns = [
    path("", homeView, name='home' ),
    path('skills', ListSkills.as_view(), name="skills_list"),
    path('jobs', ListJobs.as_view(), name='jobs'),
    path('job/<int:job_id>/apply/',ApplicationView.as_view(),name='apply'),
    path('success',ApplicationSuccessView.as_view(),name='applysuccess'),
    path('jobs/add',AddJobs.as_view(),name='addJob'),
    path('jobs/detail/<int:pk>',JobDetails.as_view(),name='jobdetail'),
    path('jobs/upd/<int:pk>',EditJobs.as_view(),name='UpdateJobs'),
    path('jobs/del/<int:pk>',DeleteJobs.as_view(),name='delete_job'),
    path('job/<int:job_id>/applicants/',showApplicants.as_view(),name='job_applicants')
]