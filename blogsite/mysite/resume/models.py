from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=122)
    desc = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.name 


    

class Resume(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    Age = models.CharField(max_length=30)
    Nationality = models.CharField(max_length=30)
    Freelance = models.CharField(max_length=30)

    Address = models.TextField(max_length=150)
    phone = models.CharField(max_length=30)
    Email = models.CharField(max_length=30)
    Skype = models.CharField(max_length=30)
    langages = models.CharField(max_length=30)
    def __str__(self):
        return self.first_name


class Post(models.Model):
    image = models.ImageField(upload_to ='images/')
    title = models.CharField(max_length=120)
    
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Project(models.Model):
    image = models.ImageField(upload_to ='images/')
    title = models.CharField(max_length=120)
    
    zip_file = models.CharField(max_length=120)
    desc = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


   

