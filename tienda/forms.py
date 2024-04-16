from django import forms
from .models import Categoria, Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'categoria']

class BusquedaForm(forms.Form):
    termino = forms.CharField(max_length=100)