from django.db import models
from django.utils import timezone

class Comentario(models.Model):
    autor = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.contenido
