from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('',views.index,name='index'),
    path('check/',views.check,name='check'),
    path('courseadded/',views.courseadded,name='courseadded'),


]