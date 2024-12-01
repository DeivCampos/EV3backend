from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Producto, Categoria
from .forms import ProductoForm, CategoriaForm
from gestorUser.views import es_administrador

@login_required
def lista_productos(request):
    if es_administrador(request.user):
        productos = Producto.objects.all()
    else:
        productos = Producto.objects.filter(usuario_creador=request.user)
    return render(request, 'gestorProductos/lista_productos.html', {'productos': productos})

@login_required
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.usuario_creador = request.user
            producto.save()
            messages.success(request, 'Producto creado exitosamente.')
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'gestorProductos/crear_producto.html', {'form': form})

@login_required
def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    
    
    if not es_administrador(request.user) and producto.usuario_creador != request.user:
        messages.error(request, 'No tienes permiso para editar este producto.')
        return redirect('lista_productos')

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()  
            messages.success(request, 'Producto actualizado exitosamente.')
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)  

    return render(request, 'gestorProductos/editar_producto.html', {'form': form, 'producto': producto})


@login_required
@user_passes_test(es_administrador)
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    messages.success(request, 'Producto eliminado exitosamente.')
    return redirect('lista_productos')

@login_required
@user_passes_test(es_administrador)
def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'gestorProductos/lista_categorias.html', {'categorias': categorias})

@login_required
@user_passes_test(es_administrador)
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría creada exitosamente.')
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'gestorProductos/crear_categoria.html', {'form': form})

@login_required
@user_passes_test(es_administrador)
def lista_categorias(request):
    print(f"Usuario actual: {request.user.username} - Admin: {request.user.is_superuser}")
    categorias = Categoria.objects.all()
    return render(request, 'gestorProductos/lista_categorias.html', {'categorias': categorias})


@login_required
@user_passes_test(es_administrador)
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría creada exitosamente.')
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'gestorProductos/crear_categoria.html', {'form': form})

@login_required
@user_passes_test(es_administrador)
def editar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría actualizada exitosamente.')
            return redirect('lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'gestorProductos/editar_categoria.html', {'form': form})

@login_required
@user_passes_test(es_administrador)
def eliminar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    categoria.delete()
    messages.success(request, 'Categoría eliminada exitosamente.')
    return redirect('lista_categorias')



