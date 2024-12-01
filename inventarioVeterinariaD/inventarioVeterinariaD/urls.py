"""
URL configuration for inventarioVeterinariaD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from gestorUser.views import registro, perfil, lista_usuarios
from gestorProductos.views import (
    lista_productos, crear_producto, editar_producto, eliminar_producto,
    lista_categorias, crear_categoria
)
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Vistas principales
    path('', views.index, name='index'),
    
    # Autenticación
    path('login/', auth_views.LoginView.as_view(template_name='gestorUser/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/', registro, name='registro'),
    
    # Perfil de usuario
    path('perfil/', perfil, name='perfil'),
    path('usuarios/', lista_usuarios, name='lista_usuarios'),
    
    # Productos
    path('productos/', lista_productos, name='lista_productos'),
    path('productos/crear/', crear_producto, name='crear_producto'),
    path('productos/editar/<int:pk>/', editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:pk>/', eliminar_producto, name='eliminar_producto'),
    
    # Categorías
    path('categorias/', lista_categorias, name='lista_categorias'),
    path('categorias/crear/', crear_categoria, name='crear_categoria'),
    path('gestorProductos/', include('gestorProductos.urls')),
]