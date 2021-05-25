from django.db import models

# Create your models here.

class Categoria(models.Model):
    titulo = models.CharField(max_length=100)
    categoria_imagen = models.ImageField(upload_to='imgs/')

    class Meta:
        verbose_name_plural='Categorias'

    def __str__(self):
        return self.titulo

class Noticia(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    detalles = models.TextField(max_length=20000)
    imagen = models.ImageField(upload_to='imgs/')
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='Noticias'
    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    comentario = models.TextField(max_length=500)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural='Comentarios'
    def __str__(self):
        return self.comentario