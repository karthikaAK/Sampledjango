from django import forms

# Register your models here.
class EmployeeInfo(forms.Form):
   name = forms.CharField()
   salary = forms.IntegerField()