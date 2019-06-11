
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login, name='login_home'),
    path('check/', views.check, name='login_check'),
]