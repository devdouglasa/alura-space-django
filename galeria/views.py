from django.shortcuts import render

from galeria.models import Fotografia

def home(request):
    fotografias = Fotografia.objects.all()

    return render(request, 'galeria/index.html', {'cards': fotografias})

def imagem(request):
    return render(request, 'galeria/imagem.html')
