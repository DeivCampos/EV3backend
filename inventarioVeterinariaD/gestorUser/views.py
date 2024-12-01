from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import RegistroUsuarioForm, PerfilUpdateForm
from .models import Perfil

def es_administrador(user):
    return user.is_superuser

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada para {username}')
            login(request, user)
            return redirect('index')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'gestorUser/registro.html', {'form': form})

@login_required
def perfil(request):
    if request.method == 'POST':
        form = PerfilUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu perfil ha sido actualizado.')
            return redirect('perfil')
    else:
        form = PerfilUpdateForm(instance=request.user)
    return render(request, 'gestorUser/perfil.html', {'form': form})

@login_required
@user_passes_test(es_administrador)
def lista_usuarios(request):
    usuarios = Perfil.objects.all()
    return render(request, 'gestorUser/lista_usuarios.html', {'usuarios': usuarios})