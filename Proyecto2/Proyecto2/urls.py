"""
URL configuration for Proyecto2 project.

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
from django.urls import path

from gestionPedidos.views import buscador_productos,buscar,contacto,MostrarPedidos,ActualizarPedido,guardarPedidoMod,Mostrarindex,eliminarPedido,MostrarClientes,MostrarCrearArticulos
from gestionPedidos.views import MostrarArticulos,eliminarCliente,eliminarArticulos,ActualizarCliente,guardarClienteMod,MostrarCrearCliente,insertarCliente,insertarArticulos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Mostrarindex),
    path('buscarProductos/', buscador_productos),
    path('buscar/', buscar),
    path('contacto/', contacto),
    path('pedidos/',MostrarPedidos,name='pedidos' ),

    path('actualizar_pedido/<int:id>',ActualizarPedido), # la pagina que tiene esta url es act.html
    path('actualizar/<int:id>',guardarPedidoMod),
    path('eliminar/<int:id>', eliminarPedido),

    path('articulos/', MostrarArticulos),
    path('eliminarArticulo/<int:id>', eliminarArticulos),
    path('crearArticulo', MostrarCrearArticulos),
    path('InsertaArt/', insertarArticulos),

       

    path('clientes/', MostrarClientes, name='clientes'),

    path('eliminarCliente/<int:id>', eliminarCliente),
 
    path('actualizar_cliente/<int:id>', ActualizarCliente), # la pagina que tiene esta url es actcli.html
    path('actualizarcli/<int:id>', guardarClienteMod),

    path('crearCliente/',MostrarCrearCliente),
    path('IngresadoCli/',insertarCliente)
    
]

