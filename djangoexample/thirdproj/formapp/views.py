from django.shortcuts import render
from . import forms

# Create your views here.
def empDetails(request):
   form= forms.EmployeeInfo()
   empInfo = {'form':form}
   return render(request,'home.html',context=empInfo)