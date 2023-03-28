from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Producto

# Create your views here.
def index(request):
    productos = Producto.objects.all()
    return render(request, 'index.html', context={'productos': productos})

def detalle(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'detalle.html', context={'producto': producto})
