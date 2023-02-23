from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings #for media
from django.conf.urls.static import static #for media
from django.contrib.auth import views as auth_views
from .views import PasswordsChangeView

urlpatterns = [
    path('reset_password/',auth_views.PasswordResetView.as_view(),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
    
    path('password/',PasswordsChangeView.as_view(template_name="change-password.html"),name="change_password"),
    path('password_success',views.password_success,name="password_success"),
]