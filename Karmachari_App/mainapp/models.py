from django.db import models

# Create your models here.
class Employee(models.Model):
    name  = models.CharField(max_length= 100, default='name')
    eid = models.CharField(max_length= 10, default="")
    phno  = models.CharField(max_length=10, default='ph no')
    email = models.CharField(max_length= 100, default='email')
    password = models.CharField(max_length= 100, default='password')