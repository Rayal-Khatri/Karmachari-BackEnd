from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth import get_user_model

User = get_user_model
# Create your views here.
def index(request):
    username =  ""
    return render(request, 'index.html', {'user': username})

def home(request):
    return render(request, 'home.html')
    
#login request gets value from action of html.login/form
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        user = auth.authenticate(username= username, password= password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Credentials Invalid")
            return redirect ('login')
    else:
        return render(request,'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/login')

def yourinformation(request):
    return render(request,'yourinformation.html')