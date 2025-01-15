from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Headers(models.Model):
    user = models.CharField(max_length=150)
    full_name = models.CharField(max_length=200)
    applying_role =  models.CharField(max_length=500)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=200)
    location = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    id =  models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.user
    
class ProfessionalExperience(models.Model):
    user = models.CharField(max_length=150)




    company1 = models.CharField(null=True,max_length=500)
    location1 = models.CharField(null=True,max_length=500)
    start_date1 = models.DateField(null=True)
    end_date1 = models.DateField(null=True)
    job_description1 = models.TextField(null=True,max_length=1000)

    company2 = models.CharField(null=True,blank=True,max_length=500)
    location2 = models.CharField(null=True,blank=True,max_length=500)
    start_date2 = models.DateField(null=True,blank=True)
    end_date2 = models.DateField(null=True,blank=True)
    job_description2 = models.TextField(null=True,blank=True,max_length=1000)

    company3 = models.CharField(null=True,blank=True,max_length=500)
    location3 = models.CharField(null=True,blank=True,max_length=500)
    start_date3 = models.DateField(null=True,blank=True)
    end_date3 = models.DateField(null=True,blank=True)
    job_description3 = models.TextField(null=True,blank=True,max_length=1000)

    company4 = models.CharField(null=True,blank=True,max_length=500)
    location4 = models.CharField(null=True,blank=True,max_length=500)
    start_date4 = models.DateField(null=True,blank=True)
    end_date4 = models.DateField(null=True,blank=True)
    job_description4 = models.TextField(null=True,blank=True,max_length=1000)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self):
        return self.user
    

class Education(models.Model):
    user = models.CharField(max_length=150)




    degree1 = models.CharField(max_length=700,null=True)
    school1 = models.CharField(max_length=700,null=True)
    cgpa1 = models.FloatField(null=True)
    start_date1 = models.DateField(null=True)
    end_date1 = models.DateField(null=True)

    degree2 = models.CharField(max_length=700,null=True,blank=True)
    school2 = models.CharField(max_length=700,null=True,blank=True)
    cgpa2 = models.FloatField(null=True,blank=True)
    start_date2 = models.DateField(null=True,blank=True)
    end_date2 = models.DateField(null=True,blank=True)

    degree3 = models.CharField(max_length=700,null=True,blank=True)
    school3 = models.CharField(max_length=700,null=True,blank=True)
    cgpa3 = models.FloatField(null=True,blank=True)
    start_date3 = models.DateField(null=True,blank=True)
    end_date3 = models.DateField(null=True,blank=True)




    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self):
        return self.user
    
class Languages(models.Model):
    user = models.CharField(max_length=150)
    languages = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self):
        return self.user
    
class Skills(models.Model):
    user = models.CharField(max_length=150)
    skills = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self):
        return self.user
    
class Hobbies(models.Model):
    user = models.CharField(max_length=150)
    hobbies = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self):
        return self.user