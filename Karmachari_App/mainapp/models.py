from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    id_user = models.IntegerField()
    profileimg = models.ImageField(upload_to='profile_images',default='img.png')
    dob = models.DateField()
    department = models.CharField(max_length=100)
    def __str__(self):
        return self.user.username
    
