from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

User = get_user_model
# Create your views here.
@login_required(login_url='/login')
def index(request):
    fullname =  request.user.get_full_name()
    context = {'fullname':fullname}
    return render(request,'Home.html',context)

    
#login request gets value from action of html.login/form
def login(request):
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
    return render(request,'your_information.html')