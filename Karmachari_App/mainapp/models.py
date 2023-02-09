from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User=get_user_model()

# Create your models here.
# deparment= (
#         ('BCT','BCT'),
#         ('BCE', 'BCE'),
#         ('BEX','BEX')
#     )

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    id_user = models.IntegerField(null=True)
    profileimg = models.ImageField(upload_to='profile_images',default='img.png')
    dob = models.DateField(auto_now=True)
    department = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=100, default=0)
    def __str__(self):
        return self.user.username

class Department(models.Model):
    name = models.CharField(max_length=100, null=True)
    Post = models.CharField(max_length=100, null=True)
    Postion = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.name

class Notice(models.Model):
    title = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(default=datetime.now)
    department = models.CharField(max_length=100, default="All Departments")
    context = models.TextField(max_length=100000, null=True)        
    def __str__(self):
        return self.title

class Leaves(models.Model):
    title = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now=True)
    department = models.CharField(max_length=100)
    subject = models.CharField(max_length=100, null=True)
    context = models.TextField(max_length=100000, null=True)
    def __str__(self):
        return self.title