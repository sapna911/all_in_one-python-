from django.contrib import admin
from django.urls import path
from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.home,name='home'),
    path('contact', views.contact,name='contact'),
    path('fun', views.fun,name='fun'),
    path('calci', views.calci,name='calci'),
    path('add', views.add,name='add'),



]
