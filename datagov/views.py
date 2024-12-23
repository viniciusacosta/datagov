from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View

app_name = 'HomePage'

def HomePage(request):
    
    return render(request, 
        'base.html',
        context={
            'text': 'estamos na home',
            'title': 'datagov'
        }

    )
