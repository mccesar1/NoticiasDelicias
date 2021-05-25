from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('todas_noticias',views.todas_noticias,name='todas_noticias'),
    path('categorias',views.categoria,name='categorias'),
    path('categoria/<int:id>',views.toda_categoria,name='toda_categoria'),
    path('detalles/<int:id>',views.detalles,name='detalles'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
