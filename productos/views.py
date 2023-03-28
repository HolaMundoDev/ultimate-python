from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Producto

# Create your views here.
def index(request):
    productos = Producto.objects.all().values()
    # productos = Producto.objects.filter(puntaje__gte=3)
    # productos = Producto.objects.get(pk=2)
    # print(productos[0].nombre)
    return JsonResponse(list(productos), safe=False)
