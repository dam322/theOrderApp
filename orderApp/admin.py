from django.contrib import admin
from orderApp.models import Order, DetallePedido
from restaurantApp.models import Restaurant
from productApp.models import Product

# Register your models here.
admin.site.register(Order)
admin.site.register(DetallePedido)
admin.site.register(Restaurant)
admin.site.register(Product)


