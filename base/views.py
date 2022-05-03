from django.http import HttpResponse
from django.shortcuts import render
from pypro.modulos import facade

def home(request):
    return render(request, 'base/home.html', {'MODULOS': facade.lista_modulos_ordenados()})
