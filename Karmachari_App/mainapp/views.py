from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from mainapp.models import Profile
from .models import Profile, Notice

# Create your views here.
@login_required(login_url='/login')
def home(request):
    fullname =  request.user.get_full_name()
    profile=Profile.objects.get(user=request.user)
    context = {'fullname':fullname,
               'profile':profile,
               }
    return render(request,'Home.html',context)


    
#login request gets value from action of html.login/form
def login(request):
    
    if request.user.is_authenticated:
         return redirect ('home')
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        user = auth.authenticate(username= username, password= password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Credentials Invalid")
            return redirect ('login')
    else:
        return render(request,'login.html')

@login_required(login_url='/login')
def logout(request):
    auth.logout(request)
    return redirect('/login')

@login_required(login_url='/login')
def yourinformation(request):
      profile=Profile.objects.get(user=request.user)
      context={
      'profile':profile,
      
    }
      return render(request,'your_information.html',context)

@login_required(login_url='/login')
def notice(request):
    # user_object = User.objects.get(username=request.user.username)
    # user_profile = Profile.objects.get(user=user_object)
    notices= Notice.objects.all()
    profile=Profile.objects.get(user=request.user)
    context={
      'profile':profile,
      'notices': notices
      
    }
    return render(request,'notices.html',context)

def postnotice(request,pk):
    notices= Notice.objects.get(id=pk)
    return render(request,'notice.html',{'notices': notices})