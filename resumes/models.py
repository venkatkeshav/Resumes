from typing import DefaultDict
from django.db import models
import uuid
from django.conf.urls.static import static
# Create your models here.

class Candidate(models.Model):
    BRANCH_OPTIONS = (('ECE','ECE'),
    ('CSE','CSE'),)
    GENDER_OPTIONS = (('MALE','MALE'),
    ('FEMALE','FEMALE'),
    ('OTHER','OTHER'))
    id = models.UUIDField(primary_key=True , default= uuid.uuid4, help_text="This is your unique id")
    First_Name = models.CharField(max_length=40, help_text="Enter your first name",default="")
    Last_Name = models.CharField(max_length=30, help_text="Enter your Last Name", default="")
    EMAil = models.EmailField(max_length=70, help_text= "Enter your Email")
    Gender = models.CharField(max_length=6,choices=GENDER_OPTIONS, help_text="Select your gender")
    Branch = models.CharField(max_length=3,choices= BRANCH_OPTIONS, help_text="Enter Your Branch")
    phone = models.IntegerField(help_text="Enter your 10 digit phone number")
    pic = models.ImageField(upload_to = 'media/pics')

    def students(self):
        num_students = Candidate.objects.all().count()
        num_ECE = Candidate.objects.filter(Branch = 'ECE').count()
        num_CSE = Candidate.objects.filter(Branch = 'CSE').count()

        context  = {
            'num_students' : num_students,
            'num_ECE' : num_ECE,
            'num_CSE': num_CSE,
        }
        return context
    

    def __str__(self):
        return f'{self.First_Name} {self.Last_Name}'
class Recuiters(models.Model):
    Name = models.CharField(max_length=100, help_text="Enter your company name in full")
    Email = models.EmailField(max_length=70 , help_text= "enter your point of contact's mail id")
    Phone = models.IntegerField(help_text="enter your 10 digit phone number")
    Job_roles = models.CharField(max_length=100, help_text="Which job roles are you searching for")
    package = models.IntegerField( help_text="enter the package you are offering")
