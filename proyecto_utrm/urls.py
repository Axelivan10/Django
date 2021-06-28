from django.contrib import admin
from django.urls import path
from ejercicio import views

urlpatterns = [
    path('', views.home, name='home'),
    path('createpassword', views.create_password, name='password'),
]
