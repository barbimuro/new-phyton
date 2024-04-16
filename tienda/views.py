from django.shortcuts import render
from .models import Categoria, Producto
from .forms import ProductoForm, BusquedaForm

def index(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    return render(request, 'tienda/index.html', {'categorias': categorias, 'productos': productos})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProductoForm()
    return render(request, 'tienda/agregar_producto.html', {'form': form})

def buscar(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            termino = form.cleaned_data['termino']
            resultados = Producto.objects.filter(nombre__icontains=termino)
            return render(request, 'tienda/resultados_busqueda.html', {'resultados': resultados})
    else:
        form = BusquedaForm()
    return render(request, 'tienda/buscar.html', {'form': form})