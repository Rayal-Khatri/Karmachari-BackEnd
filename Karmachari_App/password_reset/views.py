from django.shortcuts import render
from django.views import generic
from django.shortcuts import redirect
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
from .forms import PasswordChangingForm
from mainapp.models import *

class PasswordsChangeView(PasswordChangeView):
    form_class=PasswordChangingForm
    success_url=reverse_lazy('password_success')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        profile = Profile.objects.get(user=user)
        context['profile'] = profile
        return context
    
def password_success(request):
    return render(request,'password_change_success.html')

