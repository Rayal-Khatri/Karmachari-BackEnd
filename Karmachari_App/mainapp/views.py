from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from mainapp.models import *
from django.utils import timezone
from django.http import JsonResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return render(request,'index.html')

@login_required(login_url='login')
def home(request):
    fullname =  request.user.get_full_name()
    profile=Profile.objects.get(user=request.user)
    context = {'fullname':fullname,
               'profile':profile,
               'navbar':'home',
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
      'profile':profile,
      'navbar':'yourinformation',
      
    }
      return render(request,'your_information.html',context)

@login_required(login_url='login')
def notice(request):
    user_object = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user_object)
    notices= Notice.objects.all()
    context={
        'profile':profile,
        'notices':notices,
        'navbar':'notice',
        
    }
    return render(request,'notices.html',context)



@csrf_exempt
def checkin(request):
    # if request.is_ajax():
    if request.method == 'POST':
        print("CHECK IN")
        user = request.user
        dateOfQuestion = datetime.today()
        checkInTime = timezone.now()
        Calendar.objects.create(user=user, checkInTime=checkInTime,dateOfQuestion=dateOfQuestion)
        return JsonResponse({'in_time': checkInTime})
    response = {'message': 'Success'}
    return JsonResponse(response)

@csrf_exempt
def checkout(request):
    # if request.is_ajax():
    if request.method == 'POST':
        print("CHECK OUT") 
        user = request.user
        checkOutTime = timezone.now()
        current_calendar = Calendar.objects.filter(user=user).latest('checkInTime')
        current_calendar.checkOutTime = checkOutTime
        current_calendar.save()
        return JsonResponse({'out_time': checkOutTime})
    response = {'message': 'Success'}
    return JsonResponse(response)


# def check_in_out(request):
#     print("Checkin")
#     return redirect('/notices')


#####################################LEAVES############################################
def leaves(request):
    profile=Profile.objects.get(user=request.user)
    context={
      'profile':profile,
      'navbar':'leaves',
      }
    return render(request,'leaves.html',context)