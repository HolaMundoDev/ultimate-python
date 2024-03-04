from django.contrib import admin
from .models import Producto, Categoria
# Register your models here.

class CaterogiaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")

class ProductoModel(admin.ModelAdmin):
    # fields, campos que quiero mostrar
    # exclude, campos que no quiero mostrar
    exclude = ("creado_en",)
    list_display = ("id", "nombre", "stock", "creado_en")

admin.site.register(Producto, ProductoModel)
admin.site.register(Categoria, CaterogiaAdmin)

