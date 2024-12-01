from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    context = {
        'titulo': 'Clínica Veterinaria Chucky PB',
        'servicios': [
            'Consultas generales',
            'Vacunación',
            'Cirugías',
            'Emergencias',
            'Peluquería canina'
        ]
    }
    return render(request, 'index.html', context)