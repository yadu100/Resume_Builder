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
    company = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    job_description = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self):
        return self.user
    

class Education(models.Model):
    user = models.CharField(max_length=150)
    degree = models.CharField(max_length=700)
    school = models.CharField(max_length=700)
    cgpa = models.FloatField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
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