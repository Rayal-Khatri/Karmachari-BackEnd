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
    path('yourinformation',views.yourinformation, name='yourinformation'),
    path('notice',views.notice, name='notice'),
    path('leaves',views.leaves, name='leaves'),
    path('checkin',views.checkin,name='checkin'),
    path('checkout',views.checkout,name='checkout'),
    # path('checkin',views.checkin, name='checkin'),
    # path('checkout',views.checkout, name='checkout'),
    # # path('check_in',views.check_in_out, name='check_in_out'),
]


urlpatterns=urlpatterns+static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)