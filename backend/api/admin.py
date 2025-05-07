from django.contrib import admin
from .models import Nota, Documento, Carpeta, Etiqueta

@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_creacion', 'carpeta')
    search_fields = ('titulo', 'contenido')
    list_filter = ('carpeta',)

@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_creacion', 'carpeta')
    search_fields = ('titulo',)
    list_filter = ('carpeta',)

@admin.register(Carpeta)
class CarpetaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(Etiqueta)
class EtiquetaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)