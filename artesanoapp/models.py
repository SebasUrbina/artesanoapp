from django.db import models
from django.contrib.auth.models import User
# Create your models here.


#class Estado(models.Model):
#	nombre=models.CharField(max_length=256)
#	def __str__(self):
#		return self.nombre
class Cliente(models.Model):
	#user=models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
	nombre=models.CharField(max_length=30,null=True)
	rut=models.CharField(max_length=12,null=True)
	telefono=models.CharField(max_length=9,null=True)
	direccion=models.CharField(max_length=256,null=True)
	modelo=models.CharField(max_length=256,null=True)
	cantidad=models.CharField(max_length=256,null=True)
	instagram=models.CharField(max_length=256,null=True)
	fecha_pedido=models.CharField(max_length=256,null=True)
	fecha_envio=models.CharField(max_length=256,null=True)
	#estado=models.ForeignKey(Estado,null=True,on_delete=models.CASCADE)
	estado=models.CharField(max_length=256,null=True)
	#def __str__(self):
	#	return self.nombre
	#def __str__(self):
	#	return self.estado