from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse

app_name = 'squad'

class EducacaoHomePage(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'base.html',
            context={
                'text': 'EducacaoHomePage',
                'title': 'EDUCACAO'
            }
        )

class DetalhesSquad(View):
    pass

class ListaSeason(View):
    pass 

class DetalhesStats(View):
    pass
