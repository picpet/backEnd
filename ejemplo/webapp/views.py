from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from personas.models import Persona


def bienvenido(request):
    no_personas = Persona.objects.count()
    #personas = Persona.objects.all()
    personas = Persona.objects.order_by('nombre')

    return render(request, 'bienvenido.html', {'no_personas': no_personas, 'personas' : personas })

def login(request):
    return render(request, 'login.html')

