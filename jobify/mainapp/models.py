from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Skills(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Jobs(models.Model):
    title = models.CharField(max_length=255)
    vacancies = models.IntegerField()
    jd = models.TextField(max_length=500)
    skills = models.ManyToManyField(Skills, related_name="job_skills")
    close_date = models.DateTimeField()
    open_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Resume(models.Model):
    title = models.CharField(max_length= 255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to="resumes/")


class Applications(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    apply_date = models.DateTimeField(auto_now_add=True)
    resume = models.ForeignKey(Resume, null=True, on_delete=models.CASCADE)



