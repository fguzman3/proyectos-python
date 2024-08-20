#las vistas hacen de controller (según MVC, MVT)
from django.http import HttpResponse
import datetime, os
from django.template import Template, Context
from django.template.loader import get_template  
from django.shortcuts import render

# Cada funcion dentro del archivo views, se le llama vista

def index(request):
    return HttpResponse("Hola Mundo estamos en la raiz o index")


def saludo(request):
    return HttpResponse("Hola Mundo")

def dameFecha(request):
    fecha_actual=datetime.datetime.now()
    
    return HttpResponse(f"Fecha actual {fecha_actual}")

##En esta vista,realizó un calculo mediante un parametro que le paso a traves del url.
##Ese parametero para este ejemplo es un 

def calculaEdad(request, agno):
    edadActual = 37
    periodo = agno-2024
    edadFutura = edadActual + periodo
    documento ="<html><body><h2>En el año %s tendrás %s años </html></body></h2>"%(agno,edadFutura)
    return  HttpResponse(documento)

#pasando dos parametros a la vez mediante URL:

def calculaEdad2(request, edad,agno):
    periodo = agno-2024
    edadFutura = edad + periodo
    documento ="<html><body><h2>Tienes %s años y en el año %s tendrás %s años </html></body></h2>"%(edad,agno,edadFutura)
    return  HttpResponse(documento)


def saludoDos(request):
    ruta= os.path.abspath("Proyecto1/Templates/miplantilla_2.html")
    print(f" ESTA ES LA  RUTA {ruta}")
    docExterno=open(ruta)   #direcciono la ruta del documento y lo abro
    plt = Template(docExterno.read())  #plt es de plantilla.  aqui mediante la clase Template, le digo que es un template y la carga en memoria
    docExterno.close()   #cierro del documento.

    ctx=Context()  #aqui puedo pasar variables
    documento=plt.render(ctx)

    return HttpResponse(documento)

class Persona:
    def __init__(self, nombre, apellido_paterno, apellido_materno):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno

class Estudiante(Persona):
    def __init__(self, nombre, apellido_paterno, apellido_materno,carrera):
        super().__init__(nombre, apellido_paterno, apellido_materno)
        self.carrera = carrera
    
       
def saludoTres(request):
    ruta= os.path.abspath("Proyecto1/Templates/miplantilla_3.html")
   
    docExterno=open(ruta)   #direcciono la ruta del documento y lo abro
    plt = Template(docExterno.read())  #plt es de plantilla.  aqui mediante la clase Template, le digo que es un template y la carga en memoria
    docExterno.close()   #cierro del documento.

    persona=Persona("Amanda","Guzmán","Morles")

    #aqui puedo pasar variables por ejemplo dentro de un diccionario y hacer que el template html sea dinamico.
    ctx=Context({
        'nombre_persona': persona.nombre,
        'apellido_paterno': persona.apellido_paterno,
        'apellido_materno': persona.apellido_materno
    })
    
    documento=plt.render(ctx)

    return HttpResponse(documento)


#Definir listas y flujos de control
def saludoCuatro(request):
    plt_nro='saludo4'
    hora_actual = datetime.datetime.now().strftime('%d/%m/%Y %I:%M %p')
    
    temas=['Templates','Modelo logico','Views','Listas','Estructuras de control','CRUD','Despliegue']


    ruta= os.path.abspath("Proyecto1/Templates/miplantilla_4.html")

    docExterno=open(ruta)   #direcciono la ruta del documento y lo abro
    plt = Template(docExterno.read())  #plt es de plantilla.  aqui mediante la clase Template, le digo que es un template y la carga en memoria
    docExterno.close()   #cierro del documento.

    #aqui se pasan todas las variables que neecsite dentro de un diccionario.
    # Así se hace mas el template html dinámico.
    ctx=Context({
        'plt_nro': plt_nro,
        'hora_actual':hora_actual,
        'Listado':temas #añade al diccionario la lista creada como variable "temas"
    })
    
    documento=plt.render(ctx)

    return HttpResponse(documento)



#uso de loader , como transmisor de flujo de datos externos (plantillas)
def saludoCinco(request):
    plt_nro='saludo5'
    hora_actual = datetime.datetime.now().strftime('%d/%m/%Y %I:%M %p')
    
    estudiante=Estudiante('Fernando','Guzmán','Concha','Ingeniería Informática')

    temas=['Templates','Modelo logico','Views','Listas','Estructuras de control','CRUD','Despliegue']

    #aqui uso el metodo get_template.  (en el template mi plantilla_5 dejé comentarios de como se llega aquí)
    doc_externo=get_template('miplantilla_5.html')

    documento=doc_externo.render({
        'nombre':estudiante.nombre,
        'apellido':estudiante.apellido_paterno +" " + estudiante.apellido_materno,
        'carrera': estudiante.carrera,
        'plt_nro': plt_nro,
        'hora_actual':hora_actual,
        'Listado':temas #añade al diccionario la lista creada como variable "temas"
    })

    return HttpResponse(documento)


#uso de render , como transmisor de flujo de datos externos (plantillas) desde el modulo de django "shorcuts".
#Se eliminan las variables del método tradicional (docexterno y documento) y se pasa directo como parametro al metodo render.
#Se debe tener registrada la carpeta de los templates, como se hizo antes en setting.py

# Return: an HttpResponse whose content is filled with the result of calling django.template.loader.render_to_string() with the passed arguments.
# 
# 

def saludoSeis(request):
    plt_nro='saludo6'
    hora_actual = datetime.datetime.now().strftime('%d/%m/%Y %I:%M %p')
    
    estudiante=Estudiante('Fernando','Guzmán','Concha','Ingeniería Informática')

    temas=['Templates','Modelo lógico','Views','Listas','Estructuras de control','CRUD','Despliegue','uso de módulo loader : get_template','uso de módulo shorcuts : render']

    return render(request,'miplantilla_6.html',{
        'nombre':estudiante.nombre,
        'apellido':estudiante.apellido_paterno +" " + estudiante.apellido_materno,
        'carrera': estudiante.carrera,
        'plt_nro': plt_nro,
        'hora_actual':hora_actual,
        'Listado':temas #añade al diccionario la lista creada como variable "temas"
    })


def saludoSiete(request):
    plt_nro='saludo7'
    hora_actual = datetime.datetime.now().strftime('%d/%m/%Y %I:%M %p')
    
    estudiante=Estudiante('Fernando','Guzmán','Concha','Ingeniería Informática')

    temas=['Templates','Modelo lógico','Views','Listas','Estructuras de control','CRUD','Despliegue','uso de módulo loader : get_template','uso de módulo shorcuts : render']

    return render(request,'miplantilla_7.html',{
        'nombre':estudiante.nombre,
        'apellido':estudiante.apellido_paterno +" " + estudiante.apellido_materno,
        'carrera': estudiante.carrera,
        'plt_nro': plt_nro,
        'hora_actual':hora_actual,
        'Listado':temas #añade al diccionario la lista creada como variable "temas"
    })