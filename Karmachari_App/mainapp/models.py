from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User=get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    id_user = models.IntegerField()
    profileimg = models.ImageField(upload_to='profile_images',default='img.png')
    dob = models.DateField()
    department = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100, default=0)
    def __str__(self):
        return self.user.username
        
    
class Notice(models.Model):
    username = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=100000)
    created_at =models.DateTimeField(default=datetime.now)                                
    def __str__(self):
        return self.title