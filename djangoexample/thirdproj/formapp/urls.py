from django.contrib import admin
from django.urls import path
from formapp import views

urlpatterns = [
    path('form/',views.empDetails),
]