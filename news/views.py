from django.shortcuts import render, redirect
from .models import Noticia
from django.db.models import Q

# Create your views here.


def listar_noticias(request):
    noticias = Noticia.objects.filter(eliminado=False)  
    return render(request, 'noticias/listar_noticias.html', {'noticias': noticias})

def eliminar_noticia(request, id):
    noticia = Noticia.objects.get(pk=id)
    noticia.eliminado = True  # Marcar la noticia como eliminada
    noticia.save()
    return redirect('listar_noticias')
