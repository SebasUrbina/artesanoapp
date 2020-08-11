from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente
# Create your views here.

def index(request):
	return HttpResponse("Hello World. El-Artesano Home Page")


def home(request):
	return render(request,'artesanoapp/home.html')

def consulta(request):
	mensaje = "Rut incorrecto"

	if request.GET['rut']:
		rut =request.GET['rut']
		#cliente = Cliente.objects.filter(rut=rut_cliente)
		if len(rut)==10:
			rut_cliente=rut
			if Cliente.objects.filter(rut=rut_cliente).exists():		
				cliente= Cliente.objects.get(rut=rut_cliente)
				return render(request, "artesanoapp/estado.html",{"cliente":cliente, "rut":rut_cliente})
			else:
				rut_cliente=rut[0:2]+'.'+rut[2:5]+'.'+rut[5:8]+'-'+rut[-1]
				if Cliente.objects.filter(rut=rut_cliente).exists():		
					cliente= Cliente.objects.get(rut=rut_cliente)
					return render(request, "artesanoapp/estado.html",{"cliente":cliente, "rut":rut_cliente})
		if len(rut)==9:
			rut_cliente=rut
			if Cliente.objects.filter(rut=rut_cliente).exists():		
				rut_cliente=rut
				cliente= Cliente.objects.get(rut=rut_cliente)
				return render(request, "artesanoapp/estado.html",{"cliente":cliente, "rut":rut_cliente})
			else:
				rut_cliente=rut[0:1]+'.'+rut[1:4]+'.'+rut[4:7]+'-'+rut[-1]
				if Cliente.objects.filter(rut=rut_cliente).exists():		
					cliente= Cliente.objects.get(rut=rut_cliente)
					return render(request, "artesanoapp/estado.html",{"cliente":cliente, "rut":rut_cliente})
		else:
			return render(request,'artesanoapp/home.html',{"mensaje":"Rut no encontrado","rut":request.GET['rut']})
	else:
		return render(request,'artesanoapp/home.html',{"mensaje":"Rut no encontrado","rut":request.GET['rut']})
	#return render(request, 'artesanoapp/busqueda.html', contexto)