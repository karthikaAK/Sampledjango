from django.shortcuts import render,redirect
from modelapp.models import Employee

from django.http import HttpResponse

def add_employee(request):
    if request.method == 'POST':
        
        empNo = request.POST['empNo']
        empName = request.POST['empName']
        empSalary = request.POST['empSalary']
        empAddress = request.POST['empAddress']

        
        employee = Employee(empNo=empNo, empName=empName, empSalary=empSalary, empAddress=empAddress)
        employee.save()

        return HttpResponse('Employee added successfully!')
    else:
        return render(request, 'home.html')