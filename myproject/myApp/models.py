from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class customUser(AbstractUser):
    USER=[
        ('recruiter','Recruiter'),
        ('jobseeker','Jobseeker'),
        
    ]
    GENDER=[
        ('male','Male'),
        ('female','Female'),
    ]
    
    usertype=models.CharField(choices=USER,max_length=100,null=True)
    city=models.CharField(max_length=100,null=True)
    gender=models.CharField(choices=GENDER,max_length=100,null=True)
    email=models.EmailField(max_length=100,null=True)
    profile_pic=models.ImageField(upload_to="media/profile_pic",null=True)
    def __str__(self):
        return self.username
    
    


class JobPosting(models.Model):
    company_title = models.CharField(max_length=255)
    company_description = models.TextField()
    company_logo = models.ImageField(upload_to='logos/')
    job_title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    qualifications = models.TextField()
    application_deadline = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.job_title} at {self.company_title}"
    
