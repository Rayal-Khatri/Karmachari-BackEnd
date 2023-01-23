from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home', views.home, name="home"),
    path('Navbar', views.Navbar_Sidebar, name="Navbar"),
    #path('register', views.register, name="register"),
    path('login', views.login, name="login"),
]