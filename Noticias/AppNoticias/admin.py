from django.contrib import admin
from .models import Categoria, Noticia, Comentario

# Register your models here.

admin.site.register(Categoria)

class AdminNoticia(admin.ModelAdmin):
    list_display=('titulo','categoria','add_time')

admin.site.register(Noticia, AdminNoticia)

class AdminComentario(admin.ModelAdmin):
    list_display=('noticia','comentario','status')
admin.site.register(Comentario, AdminComentario)

