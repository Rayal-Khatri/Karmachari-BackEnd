from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime
from django.utils import timezone
from django.utils.html import format_html
from django.urls import reverse
from django.utils.html import mark_safe
from django.core.validators import RegexValidator

User=get_user_model()

# Create your models here.
# deparment= (
#         ('BCT','BCT'),
#         ('BCE', 'BCE'),
#         ('BEX','BEX')
#     )

class Post(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    designation= models.CharField(max_length=100, default="Everyone", null=True)
    salary = models.DecimalField(max_digits=8, default=10000, decimal_places=2)
    def __str__(self):
        return self.user_post

class Department(models.Model):
    dname = models.CharField(max_length=100, default="Everyone", null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    def __str__(self):
        return self.dname
    
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    userID = uuid.uuid4()
    profileimg = models.ImageField(upload_to='profile_images',default='img.png')
    dob = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=100, default=0)
    def __str__(self):
        return self.user.username
    
    def img_preview(self): #new
        return mark_safe(f'<img src = "{self.profileimg.url}" width = "300"/>')
    
class Notice(models.Model):
    title = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(default=datetime.now)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    context = models.TextField(max_length=100000, null=True)        
    def __str__(self):
        return  f"{self.title}'s notice for {self.created_at.strftime('%Y-%m-%d')}"

class Leaves(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    leave_condn = (
        ('Sick Leave','Sick Leave'),
        ('Vacation','Vacation'),
        ('Emergency','Emergency')
    )
    leave_permission = (
        ('Approved','Approved'),
        ('Pending','Pending'),
        ('Not Approved','Not Approved')
    )
    subject = models.CharField(max_length=100, null=True)
    date = models.DateField(default=timezone.now)
    duration = models.DateField(default=timezone.now)
    leave_type = models.CharField(max_length=100, null=True,choices= leave_condn)
    message = models.TextField(max_length=100000, null=True)
    status = models.CharField(max_length=100, choices= leave_permission, default='Pending')
    def __str__(self):
        return f"{self.subject}'s leaves for {self.date.strftime('%Y-%m-%d')}"
    
class Schedule(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    schedule_start = models.TimeField()
    schedule_end = models.TimeField()
    def __str__(self):
        return self.department.name
    
    
# class Payroll(models.Model):
    # status =(
    #     ('On Time','On Time'),
    #     ('Late','Late'),
    #     ('Absent','Absent'),
    # )
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
class Payroll(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    basic_pay = models.DecimalField(max_digits=8, default=10000, decimal_places=2)
    overtime = models.DecimalField(max_digits=8,null=True, decimal_places=2)
    # overtime_multiplier = models.DecimalField(max_digits=8, default= 2, decimal_places=2)
    # hours_worked = models.DecimalField(max_digits=8,default= 10, blank=True, decimal_places=2)
    deductions = models.DecimalField(max_digits=8,null=True, decimal_places=2)
    net_pay = models.DecimalField(max_digits=8,default= 0, blank=True, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)
    def calculate_net_pay(self):
        net_pay =self.basic_pay + self.overtime - self.deductions
        return(net_pay)
    
    def salary_preview(self):
        return (self.net_pay)
    
    def hour_worked_preview(self):
        return (self.hours_worked)
    
    def __str__(self):
        return f"{self.user.username}'s Payroll for {self.date.strftime('%Y-%m-%d')}"
    
class AllowedIP(models.Model):
    ip_address = models.GenericIPAddressField(null=True)
    # def __str__(self):
    #     return self.

# class Device(models.Model):
#     mac_address = models.CharField(max_length=17,)
#         # validators=[RegexValidator(
#         #     regex=r'^([0-9A-Fa-f]{2}[:]){5}([0-9A-Fa-f]{2})$',
#         #     message='MAC address must be in the format xx:xx:xx:xx:xx:xx',
#         #     code='invalid_mac_address'
#         # )]
#     # )
    
class Attendance(models.Model):
    STATUS_CHOICES = (
        ('Late', 'Late'),
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Leave', 'Leave'),
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    dateOfQuestion = models.DateField(null=True)
    checkInTime = models.DateTimeField(null=True)
    checkOutTime = models.DateTimeField(null=True)
    overtime = models.DateTimeField(null=True,blank=True)
    name=models.CharField(max_length=255,null=True)
    duration = models.FloatField(null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def save(self, *args, **kwargs):
        self.name = f"{self.user.first_name} {self.user.last_name}"
        super().save(*args, **kwargs)
        
    def calculate_duration(self):
        if self.checkOutTime:
            duration = self.checkOutTime - self.checkInTime
            return duration.total_seconds() / 3600.0  # Convert to hours
        else:
            return 0
    def __str__(self):
        return  f"{self.name}'s leaves for {self.dateOfQuestion.strftime('%Y-%m-%d')}"

class Events(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)
 
    class Meta:  
        db_table = "tblevents"
        
        