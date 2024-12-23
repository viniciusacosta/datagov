from django.urls import path
from . import views

app_name = 'educacao'
urlpatterns=[
   path('', views.EducacaoHomePage.as_view(), name='home'), 
   path('<id>/', views.DetalhesSquad.as_view(), name='squad'), 
   path('season/', views.ListaSeason.as_view(), name='season'), 
   path('stats/', views.DetalhesStats.as_view(), name='stats'), 
]
