from django.shortcuts import render
from .models import Noticia, Categoria, Comentario
from django.contrib import messages
# Create your views here.

def home(request):
    primer_noticia=Noticia.objects.first()
    tres_noticia=Noticia.objects.all()[1:3]
    tres_categoria=Categoria.objects.all()[0:3]

    return render (request, 'home.html', {
        'primer_noticia': primer_noticia,
        'tres_noticia': tres_noticia,
        'tres_categoria': tres_categoria
    })

def categoria(request,):
    categorias=Categoria.objects.all()

    return render (request, 'categorias.html',{
        'categorias': categorias
    })

def toda_categoria(request, id):

    categorias=Categoria.objects.get(id=id)
    noticia = Noticia.objects.filter(categoria=categorias)

    return render (request, 'toda_categoria.html',{
        'todas_noticias': noticia,
        'categoria': categorias

    })

def todas_noticias(request):
    todas_noticias=Noticia.objects.all()

    return render (request, 'todas_noticias.html', {
        'todas_noticias': todas_noticias
    })

def detalles(request, id):

    noticia=Noticia.objects.get(pk=id)
    if request.method == 'POST':
        nombre = request.POST['nombre']
        comentario = request.POST['mensaje']
        Comentario.objects.create(
            noticia=noticia,
            nombre=nombre,

            comentario=comentario
        )
    messages.success(request,'Comentario enviado a moderacion')
    comentario = Comentario.objects.filter(noticia=noticia, status=True).order_by('-id')
    categoria=Categoria.objects.get(id=noticia.categoria.id)
    noticia_relacionada=Noticia.objects.filter(categoria=categoria).exclude(id=id)

    return render (request, 'detalles.html', {
        'noticia': noticia,
        'noticia_relacionada': noticia_relacionada,
        'comentario': comentario
    })