"""
URL configuration for Proyecto1 project.

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

#cada vez que agrego una vista, aqui la registro como parte del URL
from django.contrib import admin
from django.urls import path

from Proyecto1.views import saludo,dameFecha,calculaEdad,calculaEdad2,saludoDos,index,saludoTres,saludoCuatro,saludoCinco,saludoSeis,saludoSiete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('saludo/',saludo),
    path('fechas/',dameFecha),
    path('edades/<int:agno>', calculaEdad), # así se pasa un parametro que lo recoge la vista
    path('calculoedad/<int:edad>/<int:agno>', calculaEdad2), # asi se pasan dos paarametros que son recogidos por la vista
    path('saludo2/', saludoDos),
    path('saludo3/', saludoTres),
    path('saludo4/', saludoCuatro),
    path('saludo5/', saludoCinco),
    path('saludo6/', saludoSeis),
    path('saludo7/', saludoSiete) 
]
