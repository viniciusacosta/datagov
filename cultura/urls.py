from django.urls import path
from . import views

app_name = 'cultura'

urlpatterns=[
    path('', views.CulturaHomePage.as_view(), name="home"),
    path('country/', views.ListaCountry.as_view(), name="country"),
    path('season/', views.ListaSeason.as_view(), name="season"),
    path('stats/', views.DetalhesStats.as_view(), name="stats"),
]
