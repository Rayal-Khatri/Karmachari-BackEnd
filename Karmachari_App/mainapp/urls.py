from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings #for media
from django.conf.urls.static import static #for media

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.login, name="login"),
    path('logout',views.logout,name='logout'),
    path('yourinformation',views.yourinformation, name='yourinformation')
]


urlpatterns=urlpatterns+static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)