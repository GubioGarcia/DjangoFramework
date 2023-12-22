from django.shortcuts import render
from django.shortcuts import get_object_or_404 

def index(request):
    context = {
        'curso': 'Programação Web com Django Framework'
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')