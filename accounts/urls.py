"""Configuração de URL para o aplicativo accounts"""
from django.urls import path, include
from . import views

app_name = 'accounts'
urlpatterns = [
    #Páginas padrão django
    path('', include('django.contrib.auth.urls')),
    #Página de cadastro
    path('register/', views.register, name='register'),
]
