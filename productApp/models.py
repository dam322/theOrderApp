from django.db import models
from restaurantApp.models import Restaurant

class Product(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    restaurante = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nombre