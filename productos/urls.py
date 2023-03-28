from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:producto_id>", views.detalle, name="producto_detalle")
]