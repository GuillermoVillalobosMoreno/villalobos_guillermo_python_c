from django.db import models
import datetime as dt

class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_registro = models.DateField("Fecha de registro",  default=dt.date.today())
    estatus = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre