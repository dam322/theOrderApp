from django import forms
from ..models import Order, DetallePedido


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['restaurante', 'cliente_nombre', 'tipo', 'estado']


class DetallePedidoForm(forms.ModelForm):
    class Meta:
        model = DetallePedido
        fields = ['producto', 'cantidad', 'observaciones', 'pedido']


DetallePedidoFormset = forms.inlineformset_factory(
    Order,
    DetallePedido,
    form=DetallePedidoForm,
    extra=1,
    can_delete=True
)
