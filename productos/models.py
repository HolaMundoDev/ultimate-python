from django.db import models
from django.utils import timezone

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    stock = models.IntegerField()
    puntaje = models.FloatField()
    # CASCADE: Si borro una categoria, borro todos los productos de esa categoria
    # PROTECT: No deja borrar la categoria
    # RESTRICT: Error si se borra sin antes borrar los productos
    # SET_NULL: Si borro la categoria, pone el campo categoria en null
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    creado_en = models.DateTimeField(default=timezone.now)