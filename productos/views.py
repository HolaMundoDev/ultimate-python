from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Producto

# Create your views here.
def index(request):
    productos = Producto.objects.all()
    return render(request, 'index.html', context={'productos': productos})

def detalle(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    return render(request, 'detalle.html', context={'producto': producto})