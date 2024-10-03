from django.db import models

# Create your models here.

class Producto(models.Model):
    id = models.CharField(primary_key=True,max_length=6)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=5,decimal_places=2)
    cantidad_en_stock = models.PositiveIntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
