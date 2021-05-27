from django.contrib import admin
from django.urls import path,include
from curd import views

urlpatterns = [
    path('',views.Home , name="home")
]
