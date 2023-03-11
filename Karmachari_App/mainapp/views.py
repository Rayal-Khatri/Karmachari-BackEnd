from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from mainapp.models import *
from django.utils import timezone
from datetime import datetime, timedelta, date
from django.views.decorators.csrf import csrf_exempt
from mainapp.utils import check_allowed_ip
from .forms import *
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO


# Create your views here.
########################HOME#########################################
def index(request):
    if check_allowed_ip(request):
        # User's IP address is allowed
        user = Profile.objects.all()
        context = {'user': user}
        return render(request, 'index.html', context)
    else:
        # User's IP address is not allowed
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
        payrolls = Payroll.objects.filter(user=user_object)[0]
        # payroll = Payroll.object.filter(user=user_object)
        if payrolls is not None:
            net_salary = payrolls.calculate_net_pay()
        payrolls.net_pay = net_salary
        payrolls.save()
    except IndexError:
        print("No payroll object found for this user")
    else:
        print("Payroll object found:", payrolls)
    
    print(net_salary)
    profile = Profile.objects.get(user=user_object)
    pays=[]
    context={
        'profile':profile,
        'navbar':'salary',
        'payrolls': payrolls,
        'net_salary': net_salary,
    }
    pays.append(context)
    return render(request,'Salary_Sheet.html', {'pays':pays})

def payroll_pdf(request):  
    user_object = User.objects.get(username=request.user.username)
    payrolls = Payroll.objects.filter(user=user_object)
    profile = Profile.objects.get(user=user_object)
    context={
        'profile':profile,
        'navbar':'payroll-pdf',
        'payrolls': payrolls,
    } 
    template_path = 'payroll_pdf.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="payroll.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pdf = pisa.CreatePDF(BytesIO(html.encode('UTF-8')), response)
    if pdf.err:
        return HttpResponse('Error generating PDF file')
    return response

