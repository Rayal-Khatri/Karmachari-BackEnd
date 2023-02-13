from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from mainapp.models import *
from mainapp.forms import *

# Create your views here.
def index(request):
    return render(request,'index.html')

@login_required(login_url='login')
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

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
def yourinformation(request):
      profile=Profile.objects.get(user=request.user)
      context={
      'profile': profile,
      'navbar':'yourinformation',
      
    }
      return render(request,'your_information.html',context)
  
@login_required(login_url='login')
def notice(request):
    notices= Notice.objects.all()
    return render(request,'notices.html', {'notices': notices})

@login_required(login_url='login')
def leaves(request):
        leaves= Leaves.objects.all()
        return render(request,'leaves.html', {'leaves': leaves})
    
@login_required(login_url='login')

def leavesform(request):
    form = LeavesForm()
    if request.method == 'POST':
        form = LeavesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leaves')
    context = {'form': form}
    return render(request, 'leavesform.html', context)

def mark_attendance(request):
    form = AttendanceForm()
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attendance = form.save(commit=False)
            attendance.attendee = request.user
            attendance.save()
            return redirect('attendance')
    return render(request, 'attendanceform.html', {'form': form})
    
