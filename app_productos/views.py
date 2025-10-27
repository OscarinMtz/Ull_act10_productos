from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Producto
from .forms import ProductoForm

def lista_productos(request):
    productos = Producto.objects.filter(activo=True)
    return render(request, 'app_productos/lista_productos.html', {'productos': productos})

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'app_productos/detalle_producto.html', {'producto': producto})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Producto creado exitosamente!')
            return redirect('app_productos:lista_productos')
    else:
        form = ProductoForm()
    
    return render(request, 'app_productos/form_producto.html', {
        'form': form,
        'titulo': 'Crear Nuevo Producto'
    })

def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Producto actualizado exitosamente!')
            return redirect('app_productos:lista_productos')
    else:
        form = ProductoForm(instance=producto)
    
    return render(request, 'app_productos/form_producto.html', {
        'form': form,
        'titulo': 'Editar Producto'
    })

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    
    if request.method == 'POST':
        producto.delete()
        messages.success(request, '🗑️ Producto eliminado exitosamente!')
        return redirect('app_productos:lista_productos')
    
    return render(request, 'app_productos/confirmar_eliminar.html', {
        'producto': producto
    })