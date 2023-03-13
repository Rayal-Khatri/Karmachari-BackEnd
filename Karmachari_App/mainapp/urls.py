from django.contrib import admin
from django.urls import path
from django.urls import re_path
from . import views
from django.conf import settings #for media
from django.conf.urls.static import static #for media

urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.login, name="login"),
    path('logout',views.logout,name='logout'),
    path('information',views.information, name='information'),
    path('notice',views.notice, name='notice'),
    path('attendance',views.attendance, name='attendance'),
    path('leaves',views.leaves, name='leaves'),
    path('checkin',views.checkin,name='checkin'),
    path('checkout',views.checkout,name='checkout'),
    path('payroll',views.payroll,name='payroll'),
    path('view_pdf/<str:pk>', views.view_pdf,name='view_pdf'),
    path('download_pdf/<str:pk>',views.download_pdf,name='download_pdf'),
    path('chart',views.chart,name='chart'),
    path('index',views.index,name='index'),
    
]


urlpatterns=urlpatterns+static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)