from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime
from django.utils import timezone
from django.utils.html import format_html
from django.urls import reverse
from django.utils.html import mark_safe
from decimal import Decimal

User=get_user_model()

# Create your models here.
# deparment= (
#         ('BCT','BCT'),
#         ('BCE', 'BCE'),
#         ('BEX','BEX')
#     )

class Department(models.Model):
    dname = models.CharField(max_length=100, default="Everyone", null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    def __str__(self):
        return self.dname
    
class Post(models.Model):
    postname= models.CharField(max_length=100, default="Everyone", null=True)
    
    def __str__(self):
        return self.post
    
class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    userID = uuid.uuid4()
    profileimg = models.ImageField(upload_to='profile_images',default='img.png')
    dob = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
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
        return self.title

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
        return self.subject
    
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
    basic_pay_rate = models.DecimalField(max_digits=8, default=10000, decimal_places=2)
    overtime = models.DecimalField(max_digits=8,null=True, decimal_places=2)
    hours_worked = models.DecimalField(max_digits=8,default= 10, blank=True, decimal_places=2)
    deductions = models.DecimalField(max_digits=8,null=True, decimal_places=2)
    net_pay = models.DecimalField(max_digits=8,null=True, blank=True, decimal_places=2)

    # def calculate_net_salary(self):
    #     gross_pay = self.hours_worked * self.basic_pay_rate
    #     net_pay = gross_pay + self.overtime - self.deductions
    #     # try:
    #     #     self.net_pay.save()
    #     # except AttributeError:
    #     #     print("Couldn't save image {}".format(net_pay))
    #     if net_pay is not None:
    #         net_pay.save()
        

    # def save(self, *args, **kwargs):
    #     self.net_salary = self.calculate_net_salary()
    #     super(Payroll, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.user.username
    
class AllowedIP(models.Model):
    ip_address = models.GenericIPAddressField(null=True)
    # def __str__(self):
    #     return self.
    
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

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        self.name = f"{self.user.first_name} {self.user.last_name}"
        super().save(*args, **kwargs)
        
    def calculate_duration(self):
        if self.checkOutTime:
            duration = self.checkOutTime - self.checkInTime
            return duration.total_seconds() / 3600.0  # Convert to hours
        else:
            return 0

class Events(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)
 
    class Meta:  
        db_table = "tblevents"
        
        