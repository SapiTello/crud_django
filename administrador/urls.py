from django.urls import path
from .import views

urlpatterns = [
    path('',views.home),
    path('registrarProducto/',views.registrarProducto),
    path('edicionProducto/<id>',views.edicionProducto),
    path('editarProducto/',views.editarProducto),
    path('eliminarProducto/<id>',views.eliminarProducto),
]