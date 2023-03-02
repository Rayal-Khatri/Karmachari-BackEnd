from django.shortcuts import render
from django.views import generic
from django.shortcuts import redirect
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
from .forms import PasswordChangingForm

class PasswordsChangeView(PasswordChangeView):
    form_class=PasswordChangingForm
    success_url=reverse_lazy('password_success')
    
def password_success(request):
    return render(request,'password_change_success.html')

