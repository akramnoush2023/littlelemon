from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.sayHello, name='sayHello'),
    path('home/', views.index, name='index'),
]