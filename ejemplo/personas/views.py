from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from personas.models import Persona


def detallePersona(request, id):
    #persona = Persona.objects.get(pk=id)
    persona = get_object_or_404(Persona,pk=id)
    return render(request, 'personas/detalle.html', {'persona' : persona})


PersonaForm = modelform_factory(Persona, exclude=[])

def nuevaPersona(request):
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST) #Obtenemos la informacion del formulario

        if formaPersona.is_valid(): #validamos que el formulario sea valido

            formaPersona.save()#Se hace el insert en la base de datos
            return redirect('index')

    else:
        formaPersona = PersonaForm()

    return render(request, 'personas/editar.html', {'formaPersona': formaPersona})

def editarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)

    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST, instance=persona) #Obtenemos la informacion del formulario

        if formaPersona.is_valid(): #validamos que el formulario sea valido

            formaPersona.save()#Se hace el insert en la base de datos
            return redirect('index')

    else:

        formaPersona = PersonaForm(instance= persona)

    return render(request, 'personas/editar.html', {'formaPersona': formaPersona})


def eliminarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)

    if persona:
        persona.delete()
        return redirect('index')
