from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def index(request):
    name =  'Haemon'
    return render(request, 'index.html', {'name': name})

#creating a sign up page
def register(request):
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.Post["email"]
        password = request.Post["password"]
        password2 = request.Post["password2"]
        
        if password==password2:
            if User.obects.filter(email=email).exists():
                messages.info(request, "Email Already Used")
                return redirect('register')
            elif User.object.filter(username=username).exists():
                messages.info(request, "Username Already Used")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, "Password did not match")
            return redirect('register')
    else:    
        return render(request,'register.html')
    
#login
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username= username, password= password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Credentials Invalid")
            return redirect ('login')
    else:
        return render(request,'login.html')