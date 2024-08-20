from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from gestionPedidos.models import Articulos
from gestionPedidos.models import Clientes
from gestionPedidos.form import FormularioContacto
from django.core.mail import send_mail
from django.conf import settings
from gestionPedidos.models import Pedidos
from datetime import datetime
from django.db import IntegrityError

# Create your views here.

def buscador_productos(request):

    return render(request,"buscador_productos.html")



def buscar(request):
    p = request.GET['prd']
    print(p)

    if len(p)>20:
         msj="Error: texto demasiado largo"

    elif p:
          
            articulos=Articulos.objects.filter(nombre__icontains=p)
            return render(request,"resultados_busqueda.html",
                        {"articulos":articulos,
                        "query": p
                        })
    else:
            msj="Falta ingresar registro"
    return HttpResponse(msj)


def contacto(request):
       if request.method == 'POST':
        subject = request.POST["asunto"]

        message = request.POST["mensaje"] + " " + request.POST["email"]

        email_from = settings.EMAIL_HOST_USER
        recipient_list = ["fernando.guzmanconcha@gmail.com"]

        send_mail(subject, message, email_from, recipient_list)


        return render(request, 'gracias.html')
      
       return render(request, 'contacto.html')

#Index:
def Mostrarindex(request):
     hora_actual = datetime.now().strftime('%d/%m/%Y %I:%M %p')
     return render(request,"index.html",{'hora_actual':hora_actual})

#Pedidos:
def MostrarPedidos(request):
    registro_pedidos = Pedidos.objects.all().values()  
    return render(request,"pedidos.html",{"ped":registro_pedidos})

#Selecciona y muestra el pedido a actualizar. 
def ActualizarPedido(request,id):
    registro_pedidos = Pedidos.objects.get(id=id)
    articulos = Articulos.objects.all
    clientes = Clientes.objects.all
    return render(request,"act.html",{"ped":registro_pedidos,"articulos":articulos, "clientes":clientes })

#Guarda los cambios, muestra el pedido actualizado y muestra un mensaje de OK. 
def guardarPedidoMod(request,id):
    if request.method == 'POST':
       registro_pedidos = Pedidos.objects.get(id=id)
       nuevo_codigo_art= int( request.POST['opciones_articulos'])
       nuevo_rut=  request.POST['opciones_rut']
       nueva_fecha = request.POST['fecha']
       nuevo_nropedido = request.POST['numero_pedido']
                   
       try:
            nuevo_entrega = request.POST['entrega']
       except KeyError:
            nuevo_entrega = False
       
       print (nuevo_codigo_art)
       print (nuevo_rut)
       print (nueva_fecha)
       print (nuevo_entrega)

       try:
            articulo = get_object_or_404(Articulos, codigo_art=nuevo_codigo_art)
            cliente = get_object_or_404(Clientes, rut=nuevo_rut)

       except ValueError:
            msj2='Error: Código de artículo inválido'
            return render(request, 'act.html', {"ped": registro_pedidos, "msj":msj2 })
       print (nuevo_entrega)
       registro_pedidos.codigo_art = articulo
       registro_pedidos.rut = cliente
       registro_pedidos.fecha = datetime.strptime(nueva_fecha, "%Y-%m-%d").date()
       registro_pedidos.numero= nuevo_nropedido
       registro_pedidos.entregado= nuevo_entrega
       
       registro_pedidos.save()
       print (registro_pedidos.fecha)
       msj="Datos Modificados con éxito"

    # return redirect('pedidos') 
    return render(request,'actualizado.html',{"ped":registro_pedidos,"msj":msj})

def eliminarPedido(request,id):
    try:
       registro_pedidos = Pedidos.objects.get(id=id)
       registro_pedidos.delete()
       registro_pedidos=Pedidos.objects.all().values()
       msj="Registro eliminado con éxito"
       
       return render(request,"pedidos.html",{"ped":registro_pedidos,"msj":msj})
    
    except:
       registro_pedidos=Pedidos.objects.all().values()
       msj2="No existe registro a eliminar"
       return render(request,"pedidos.html",{"ped":registro_pedidos,"msj":msj2})

def insertarPedidos(request):
     #  if request.method == 'POST':
     #       nombre = request.POST.get('nombre')
     #       rut = request.POST.get('rut')
     #       direccion = request.POST.get('direccion')
     #       email = request.POST.get('email')
     #       telefono = request.POST.get('telefono')

     #       if rut and nombre:
     #            nuevo_cliente = Clientes(nombre=nombre, rut=rut, direccion=direccion, telefono=telefono)
     #            nuevo_cliente.save()
     #       return redirect('ingreso_articulos')
     #  else:
           pass   

# FGC: 07.09.2024
# Falta crear metodos para insertar pedidos.
# Falta crear metodos para editar y guardar en articulos. (Eliminar ya existe)


#CLIENTES:
def MostrarClientes(request):
     registro_clientes=Clientes.objects.all().values()

     return render(request,'clientes.html',{"cli":registro_clientes})
#Muestra la URL para crear un cliente
def MostrarCrearCliente(request):
     return render(request,'crearcliente.html')

#permite crear un cliente en la BD
def insertarCliente(request):
      if request.method == 'POST':
           nombre = request.POST.get('nombre')
           rut = request.POST.get('rut')
           direccion = request.POST.get('direccion')
           email = request.POST.get('email')
           telefono = request.POST.get('telefono')

           if rut and nombre:
                try:
                    nuevo_cliente = Clientes(nombre=nombre, rut=rut, direccion=direccion, telefono=telefono,email=email)
                    nuevo_cliente.save()
                    msj = 'Cliente ingresado con exito'
                    registro_clientes=Clientes.objects.all().values()
                    return render(request,"clientes.html",{"cli":registro_clientes,"msj":msj})
                except IntegrityError:
                     msj2 = 'El rut ya existe. No se puede ingresar un cliente con el mismo rut.'
                     registro_clientes = Clientes.objects.all().values()
                return render(request, "clientes.html", {"cli":registro_clientes, "msj2":msj2})

      else:
           msj2 = 'No se puede ingresar cliente sin nombre o rut'
           return render(request,"clientes.html",{"msj2":msj2})

#Selecciona y muestra el cliente a actualizar. 
def ActualizarCliente(request,id):
    registro_clientes = Clientes.objects.get(id=id)
    return render(request,"actcli.html",{"cli":registro_clientes })

#Guarda los cambios, muestra el cliente actualizado y muestra un mensaje de OK.
def guardarClienteMod(request,id):
     if request.method == 'POST':
        try:
            registro_clientes = Clientes.objects.get(id=id)
            # nuevo_rut = request.POST['rut'] no actualizará el rut puesto que afecta la integridad referencial. Lo mejor es eliminar el rut.
            nuevo_nombre = request.POST['nombre']
            nuevo_direccion = request.POST['direccion']
            nuevo_telefono = request.POST['telefono']
            nuevo_email = request.POST['email']
            

            # registro_clientes.rut=nuevo_rut
            registro_clientes.nombre=nuevo_nombre
            registro_clientes.telefono=nuevo_telefono
            registro_clientes.direccion=nuevo_direccion
            registro_clientes.email=nuevo_email
        
        except:
            registro_clientes=Clientes.objects.all().values()
            msj2="No se pudo actualizar"
            return (request,'actcli.html',{"cli":registro_clientes,"msj":msj2})
        
        registro_clientes.save() #guardo los cambios.
        msj="Datos de clientes modificados con éxito"
        print (registro_clientes.rut)

     return render(request,'actualizadocli.html',{"cli":registro_clientes,"msj":msj})

#Permite eliminar un cliente seleccionado
def eliminarCliente(request,id):
    try:
       registro_clientes = Clientes.objects.get(id=id)
       registro_clientes.delete()
       registro_clientes=Clientes.objects.all().values()
       msj="Registro de Cliente eliminado con éxito"
       
       return render(request,"clientes.html",{"cli":registro_clientes,"msj":msj})
    
    except:
       registro_clientes=Clientes.objects.all().values()
       msj2="No existe cliente a eliminar"
       return render(request,"clientes.html",{"cli":registro_clientes,"msj":msj2})


# ARTICULOS:
#Muestra toda la nomina de articulos existentes.
def MostrarArticulos(request):
     registro_articulos=Articulos.objects.all().values()

     return render(request,'articulos.html',{"art":registro_articulos})

#muestra la url para crear un articulo.
def MostrarCrearArticulos(request):
     return render(request,'creararticulo.html')

#permite crear el articulo en la BD
def insertarArticulos(request):
    if request.method == 'POST':
      
        cod_art = request.POST.get('cod_art')   # hago esto para majenar un error, en que el usuario ingrese un producto nulo.  solo se ejecutará el bloque si el campo cod_art existe (no es nulo).
        if cod_art:
            
             cod_art = int(request.POST.get('cod_art'))
             nombre = request.POST.get('nombre')
             seccion = request.POST.get('seccion')
             precio = int(request.POST.get('precio'))

        else:
           msj2 = 'El código de articulo es obligatorio.'
           registro_articulos = Articulos.objects.all().values()
           return render(request, "articulos.html", {"art": registro_articulos, "msj2": msj2})

        try:
            if cod_art and (precio is not None and precio > 0):
                    nuevo_articulo = Articulos(codigo_art=cod_art, nombre=nombre, seccion=seccion, precio=precio)
                    nuevo_articulo.save()
                    msj = 'Producto ingresado con exito'
                    registro_articulos = Articulos.objects.all().values()
                    return render(request, "articulos.html", {"art":registro_articulos, "msj":msj})
        except IntegrityError:
                    msj2 = 'El código de articulo ya existe. No se puede ingresar un producto con el mismo código.'
                    registro_articulos = Articulos.objects.all().values()
                    return render(request, "articulos.html", {"art":registro_articulos, "msj2":msj2})
          
        except ValueError:
               msj2 = 'El precio debe ser un número válido.'
               registro_articulo = Articulos.objects.all().values()  # Cambié Clientes por Articulos aquí
               return render(request, "articulos.html", {"art": registro_articulo, "msj2": msj2})

    else:
        msj2 = 'No se puede ingresar artículo sin código o precio'
        return render(request, "articulos.html", {"msj2":msj2})

#permite eliminar un articulo seleccionado
def eliminarArticulos(request,id):
    try:
       registro_articulo = Articulos.objects.get(id=id)
       registro_articulo.delete()
       registro_articulo=Articulos.objects.all().values()
       msj="Artículo eliminado con éxito"
       
       return render(request,"articulos.html",{"art":registro_articulo,"msj":msj})
    
    except:
       registro_articulo=Articulos.objects.all().values()
       msj2="No existe artículo a eliminar"
       return render(request,"articulos.html",{"art":registro_articulo,"msj2":msj2})

