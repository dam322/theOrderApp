from django.db import models
from productApp.models import Product
from restaurantApp.models import Restaurant


# Create your models here.
class Order(models.Model):
    ESTADO_CHOICES = (
        (1, 'En espera'),
        (2, 'En preparación'),
        (3, 'Listo para recoger'),
    )
    TIPO_CHOICES = (
        (1, 'Para llevar'),
        (2, 'Consumo en el sitio'),
    )

    cliente_nombre = models.CharField(max_length=255)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    estado = models.IntegerField(choices=ESTADO_CHOICES, default=1, blank=True, null=True)
    tipo = models.IntegerField(choices=TIPO_CHOICES)
    restaurante = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return f"Pedido #{self.id} - {self.cliente_nombre}"


class DetallePedido(models.Model):
    pedido = models.ForeignKey(Order, on_delete=models.CASCADE)
    producto = models.ForeignKey(Product, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.producto.nombre} - {self.cantidad}"
