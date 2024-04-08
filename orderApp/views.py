from django.shortcuts import render
from productApp.models import Product
from restaurantApp.models import Restaurant
from .forms.forms import PedidoForm, DetallePedidoFormset
from .models import DetallePedido, Order


def index(request):
    restaurantes = Restaurant.objects.all()
    return render(request, 'index.html', {'restaurantes': restaurantes})


def menu(request, restaurante_id):
    restaurante = Restaurant.objects.get(id=restaurante_id)
    productos = Product.objects.filter(restaurante=restaurante)
    return render(request, 'menu.html', {'restaurante': restaurante, 'productos': productos})


def pedido(request, restaurante_id):
    # Ultimo ctl + z
    pedido = None
    detalles = None
    restaurante = Restaurant.objects.get(id=restaurante_id)
    producto = Product.objects.filter(restaurante=restaurante)
    algo = True
# extra=3 para mostrar 3 formularios de detalle por defecto

    if request.method == "POST":
        pedido_form = PedidoForm(request.POST)
        formset = DetallePedidoFormset(request.POST)

        if algo:
            pedido = pedido_form.save()
            pedido.restaurante = restaurante
            pedido.save()
            for form in formset:
                detalle = form.save(commit=False)
                detalle.pedido = pedido
                detalle.save()

            # return redirect('pedido_detalle', pk=pedido.pk)
    else:
        pedido_form = PedidoForm()
        formset = DetallePedidoFormset()

    context = {
        'pedido': pedido,
        'detalles': detalles,
        'pedido_form': pedido_form,
        'formset': formset,
        'restaurante': restaurante,
        'productos': producto
    }
    return render(request, 'pedido.html', context)


def pedido_detalle(request, pedido_id):
    pedido = Order.objects.get(id=pedido_id)
    detalles = DetallePedido.objects.filter(pedido=pedido)
    return render(request, 'pedido_detalle.html', {'pedido': pedido, 'detalles': detalles})