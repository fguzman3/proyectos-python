from django.contrib import admin
from .models import Clientes,Articulos,Pedidos


## para que las tablas creadas en la base de datos sean visibles en el admin de django,
# se deben registrar

class ClientesAdmin(admin.ModelAdmin):
    list_diplay=["nombre","direcion","telefono"]
    search_fields=("nombre","telefono")

admin.site.register(Clientes,ClientesAdmin)

admin.site.register(Articulos)

admin.site.register(Pedidos)