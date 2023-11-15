from django.shortcuts import render
import datetime


def display(request):
    date = datetime.datetime.now()
    hour = int(date.strftime('%H'))
    if hour<12:
        now = 'Good Morning'
    else:
       now = "Good evening"
    date_dict = {
        'display_date':date,
        'name':"karthika",
        'greetings':now
        }
    
    return render(request, 'home.html',context= date_dict)

