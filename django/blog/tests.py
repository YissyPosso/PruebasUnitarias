from django.test import TestCase
from .models import Comentario

class ComentarioModelTest(TestCase):
    def test_str_representation(self):
        comentario = Comentario(autor="Maria Martinez", contenido="Este es un comentario de prueba")
        self.assertEqual(str(comentario), "Este es un comentario de prueba")

    def test_fecha_comentario_predeterminada(self):
        comentario = Comentario(autor="Maria Martinez", contenido="Otro comentario de prueba")
        comentario.save()
        self.assertIsNotNone(comentario.fecha_comentario)


