from django.contrib import admin
from modelapp.models import Employee


# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    emp_details = ['empNo', 'empName', 'empSalary', 'empAddress']

admin.site.register(Employee, EmployeeAdmin)