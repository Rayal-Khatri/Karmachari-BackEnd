from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages

# Create your views here.
def index(request):
    features = "some features"
    return render(request, 'index.html', {'features': features})

def home(request):
    return render(request, 'home.html')

def Navbar_Sidebar(request):
    return render(request, 'Navbar_Sidebar.html')

    
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