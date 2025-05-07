from django.db import models

class Carpeta(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Nota(models.Model):
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    carpeta = models.ForeignKey(Carpeta, on_delete=models.CASCADE, related_name='notas', null=True, blank=True)
    etiquetas = models.ManyToManyField(Etiqueta, blank=True)

    def __str__(self):
        return self.titulo

class Documento(models.Model):
    titulo = models.CharField(max_length=255)
    archivo = models.FileField(upload_to='documentos/')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    carpeta = models.ForeignKey(Carpeta, on_delete=models.CASCADE, related_name='documentos', null=True, blank=True)

    def __str__(self):
        return self.titulo