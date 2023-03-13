from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from mainapp.models import *
from django.utils import timezone
from datetime import datetime, timedelta, date
from django.views.decorators.csrf import csrf_exempt
from mainapp.utils import *
from .forms import *


# Create your views here.
########################HOME#########################################
def index(request):
    # devices = Device.objects.prefetch_related('related_field')
    # for device in devices:
    #     device.related_field.get_mac_address()
    # # mac_address = Device.mac_address.get_mac_address(request)
    # # device = Device(mac_address='01:23:45:67:89:ab')
    # device.save()
    # print(device)
    # context = {'device':device}
    # return render(request, 'index.html', context)
    
    # if check_allowed_ip(request):
    #     # User's IP address is allowed
    #     user = Profile.objects.all()
    #     context = {'user': user}
    #     return render(request, 'index.html', context)
    # else:
    #     # User's IP address is not allowed
    return HttpResponse('Access Denied')

@login_required(login_url='login')
def home(request):
    fullname =  request.user.get_full_name()
    profile=Profile.objects.get(user=request.user)
    context = {'fullname':fullname,
               'profile':profile,
               'navbar':'home',
               }
    return render(request,'Home.html',context)


########################LOGIN#########################################      
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

########################LOGOUT#########################################
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')


########################YOUR INFORMATION#########################################
@login_required(login_url='login')
def information(request):
      profile=Profile.objects.get(user=request.user)
      context={
      'profile':profile,
      'navbar':'yourinformation',
      
    }
      return render(request,'your_information.html',context)


########################NOTICE#########################################
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


########################ATTENDANCE#########################################
@login_required(login_url='login')
def attendance(request):
    user_object = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user_object)
    notices= Notice.objects.all()
    context={
        'profile':profile,
        'notices':notices,
        'navbar':'attendance',   
    }
    return render(request,'attendance.html',context)
    
    

########################CHECKED IN#########################################
@csrf_exempt
def checkin(request):
    # if request.is_ajax():
    if request.method == 'POST':
        print("CHECK IN")
        user = request.user
        dateOfQuestion = datetime.today()
        checkInTime = timezone.now()
        Attendance.objects.create(user=user, checkInTime=checkInTime,dateOfQuestion=dateOfQuestion)
        return JsonResponse({'in_time': checkInTime})
    response = {'message': 'Success'}
    return JsonResponse(response)


########################CHECKED OUT#########################################
@csrf_exempt
def checkout(request):
    # if request.is_ajax():
    if request.method == 'POST':
        print("CHECK OUT") 
        user = request.user
        checkOutTime = timezone.now()
        current_attendance = Attendance.objects.filter(user=user).latest('checkInTime')
        current_attendance.checkOutTime = checkOutTime
        current_attendance.save()
        duration = current_attendance.calculate_duration()

        # Get the schedule of the user's department
        profile = Profile.objects.get(user=request.user)
        department = profile.department.id
        schedule = Schedule.objects.get(department=department)
        late_time = datetime.combine(date.today(), schedule.schedule_start) + timedelta(minutes=15)
        late_time = late_time.time()
        attendance_date = date.today()


        # Determine the status based on the schedule and check-in time
        if current_attendance.checkInTime.time() > late_time:
            status = 'Late'  # Late
        elif current_attendance.checkOutTime.time() < schedule.schedule_end:
            status = 'Leave'  # Leave
        elif duration > (schedule.schedule_end - schedule.schedule_start).total_seconds() / 3600.0:
            status = 'Absent'  # Absent
        else:
            status = 'Present'  # Presents
    try:
        attendance = Attendance.objects.filter(user=user, dateOfQuestion=attendance_date).latest('checkInTime')
    except Attendance.DoesNotExist:
        attendance = None

    # If an attendance object already exists, update its checkOutTime, duration, and status
    if attendance is not None:
        attendance.checkOutTime = checkOutTime
        attendance.duration = duration
        attendance.status = status
        attendance.save()
    else:
        # Create a new attendance object
        attendance = Attendance.objects.create(
            user=user,
            name=profile.user.get_full_name(),
            duration=duration,
            status=status,
            dateOfQuestion=attendance_date,
            checkOutTime=checkOutTime,
        )

        return JsonResponse({'out_time': checkOutTime, 'duration': duration})
    response = {'message': 'Success'}
    return JsonResponse(response)





#####################################LEAVES############################################
@login_required(login_url='login')
def leaves(request):
    leaves= Leaves.objects.filter(user_id=request.user.id)
    submitted=False
    profile=Profile.objects.get(user=request.user)
    form = LeavesForm()
    if request.method == 'POST':
        form = LeavesForm(request.POST)
        if form.is_valid():
            form.instance.user_id = request.user.id
            # Leaves = form.save(commit=False)
            # Leaves.user = request.user
            form.save()
            return HttpResponseRedirect('leaves?submitted=True')
    else:
        form=LeavesForm()
        if 'submitted in request.GET':
            submitted=True
            context={
            'profile':profile,
            # 'navbar':'leaves',
            'form': form,
            'submitted':submitted,
            'leaves':leaves,
            }
            return render(request,'leaves.html',context)

########################PAYROLL######################################### 
@login_required(login_url='login')
def payroll(request):
    user_object = User.objects.get(username=request.user.username)
    try:
        payrolls = Payroll.objects.filter(user=user_object)
        # payroll = Payroll.object.filter(user=user_object)
        for payroll in payrolls:
            if payroll is not None:
                net_salary = payroll.calculate_net_pay()
            payroll.net_pay = net_salary
            payroll.save()
    except IndexError:
        print("No payroll object found for this user")
    else:
        print("Payroll object found:", payrolls)
    # for i in payrolls:
    #     print(i)
    # print(net_salary)
    profile = Profile.objects.get(user=user_object)
    context={
        'profile':profile,
        'navbar':'Salary;-Sheet',
        'payrolls': payrolls,
        'net_salary': net_salary,
    }
    return render(request,'Salary_Sheet.html', context)

########################VIEW PAYROLL PDF######################################### 
def view_pdf(request, pk):
    user_object = User.objects.get(username=request.user.username)
    payroll = Payroll.objects.filter(user=user_object, id=pk)[0]
    profile = Profile.objects.get(user=user_object)
    data = {
            'payroll': payroll,
            'user': user_object,
            'profile': profile,
            }
    pdf = render_to_pdf('payroll_pdf.html', data)
    return HttpResponse(pdf, content_type='application/pdf')

########################DOWNLOAD PAYROLL PDF######################################### 
def download_pdf(request, pk):
    user_object = User.objects.get(username=request.user.username)
    payroll = Payroll.objects.filter(user=user_object, id=pk)[0]
    profile = Profile.objects.get(user=user_object)
    data = {
            'payroll': payroll,
            'user': user_object,
            'profile': profile,
            }	
    pdf = render_to_pdf('payroll_pdf.html', data)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="payroll.pdf"'
    return response

########################CHART######################################### 
def chart(request):
    user_object = User.objects.get(username=request.user.username)
    payroll = Payroll.objects.filter(user=user_object)
    profile = Profile.objects.get(user=user_object)	
    context={
            'payroll': payroll,
            'user': user_object,
            'profile': profile,
    }
    return render(request,'chart.html', context)