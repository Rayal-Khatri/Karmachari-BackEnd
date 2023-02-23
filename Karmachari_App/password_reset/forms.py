from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms


class PasswordChangingForm(PasswordChangeForm):
    old_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'Answer_pw','placeholder':'Old Password'}))
    new_password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'Answer_pw','placeholder':'New Password'}))
    new_password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'Answer_pw','placeholder':'Confirm New Password'}))
    
    class meta:
        model=User
        fields=('old_password','new_password1','new_password2')
