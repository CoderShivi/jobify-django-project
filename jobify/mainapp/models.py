from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Skills(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
class JobType(models.Model):
    title=models.CharField(max_length=255)

    def __str__(self):
        return self.title
    

    
class SalaryType(models.TextChoices):
    PER_MONTH = 'Per Month'
    PER_YEAR = 'Per Year'

class Jobs(models.Model):
    title = models.CharField(max_length=255)
    vacancies = models.IntegerField()
    jd = models.TextField(max_length=500)
    skills = models.ManyToManyField(Skills, related_name="job_skills")
    open_date = models.DateTimeField(auto_now_add=True)
    close_date = models.DateTimeField()
    salary=models.DecimalField(max_digits=10,decimal_places=2,null=True)
    jobType=models.ManyToManyField(JobType,related_name="job_type")
    salary_based_on = models.CharField(
        max_length=20,
        choices=SalaryType.choices,
        default=SalaryType.PER_MONTH
    )

    

    def __str__(self):
        return self.title

class Resume(models.Model):
    title = models.CharField(max_length= 255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to="resumes/")


class Applications(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    email=models.EmailField(default='user@gmail.com')
    phone=models.CharField(max_length=15,default='000-000-0000')
    apply_date = models.DateTimeField(auto_now_add=True)
    resume = models.ForeignKey(Resume, null=True, on_delete=models.CASCADE)
    cover_letter=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.applicant_name
    


