from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings #for media
from django.conf.urls.static import static #for media

urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.login, name="login"),
    path('logout',views.logout,name='logout'),
    path('yourinformation',views.yourinformation, name='yourinformation'),
    path('notice',views.notice, name='notice'),
    path('postnotice/<str:pk>',views.postnotice, name='postnotice'),
]


urlpatterns=urlpatterns+static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)