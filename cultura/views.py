from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView 
from django.views.generic import TemplateView
from django.views import View

app_name = 'cultura'

class CulturaHomePage(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'base.html',
            context={
                'text': 'CulturaHomePage',
                'title': 'CulturaHomePage'
            }
        )
    
class ListaCountry(View):
    pass

class ListaSeason(View):
    pass
 
class DetalhesStats(View):
    pass
