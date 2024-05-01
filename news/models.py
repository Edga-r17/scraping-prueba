from django.db import models

# Create your models here.
class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    autor = models.CharField(max_length=100)
    fecha_publicacion = models.DateTimeField()
    eliminado = models.BooleanField(default=False)  

    def __str__(self):
        return self.titulo