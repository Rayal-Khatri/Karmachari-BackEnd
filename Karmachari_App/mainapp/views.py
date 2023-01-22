from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Employee

# Create your views here.
def index(request):
    features = Employee.objects.all()
    return render(request, 'index.html', {'features': features})

def home(request):
    return render(request, 'home.html')


    
#login request gets value from action of html.login/form
def login(request):
    if request.method == 'POST':
        eid = request.POST['eid']
        password = request.POST['password']

        user = auth.authenticate(eid= eid, password= password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Credentials Invalid")
            return redirect ('login')
    else:
        return render(request,'login.html')