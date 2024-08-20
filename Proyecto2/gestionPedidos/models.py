from django.db import models

# Create your models here.

#Aqui se debe crear una clase por cada tabla o entidad que se necesite


class Clientes(models.Model):
    
    rut=models.CharField(max_length=20,
                blank=True,
                null=True,
                default=None, 
                unique=True)
    nombre=models.CharField(
            max_length=100)
    direccion=models.CharField(
              max_length=100,
              verbose_name='DIRECCION DEL CLIENTE')   
    email=models.EmailField(
          blank=True,
          null=True )
    telefono=models.CharField(
                max_length=10,
                blank=True,
                null=True)
    
    def __str__(self):
        return f'RUT: {self.rut} ID:{self.id}  '

class Articulos(models.Model):
        codigo_art=models.IntegerField(default=0, unique=True)
        nombre=models.CharField(max_length=100)
        seccion=models.CharField(max_length=100)
        precio=models.IntegerField()

        def __str__(self):
            return f'Codigo Art.: {self.codigo_art} ID:{self.id} '        

class Pedidos(models.Model):
      numero=models.IntegerField()
      fecha=models.DateField()
      entregado=models.BooleanField()
      codigo_art=models.ForeignKey(Articulos, on_delete=models.CASCADE, to_field='codigo_art')
      rut=models.ForeignKey(Clientes,on_delete=models.CASCADE,to_field='rut')  
                                    
       

      def __str__(self):
            return f'Número pedido: {self.numero}/ Fecha del pedido: {self.fecha} / Entregado a cliente:{self.entregado}'


# Nota: # on_delete=models.CASCADE 
# indica que si se elimina un árticulo o cliente, 
# también se eliminarán todos los pedidos asociados a articulo o cliente.