from django.shortcuts import render, redirect
from .models import Producto

# Create your views here.

def home(request):
    producto = Producto.objects.all()
    return render(request,"gestionProductos.html",{"productos":producto})

def registrarProducto(request):
    id = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    descripcion = request.POST['txtDescripcion']
    precio = request.POST['txtPrecio']
    cantidad_en_stock = request.POST['txtStock']

    producto = Producto.objects.create(id=id, nombre=nombre, descripcion=descripcion, precio = precio, cantidad_en_stock = cantidad_en_stock) 
    return redirect('/')

def edicionProducto(request,id):
    producto = Producto.objects.get(id=id)
    return render(request,"edicionProducto.html",{"producto": producto})

def editarProducto(request):
    id = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    descripcion = request.POST['txtDescripcion']
    precio = request.POST['txtPrecio']
    cantidad_en_stock = request.POST['txtStock']

    producto = Producto.objects.get(id=id)
    producto.nombre = nombre
    producto.descripcion = descripcion
    producto.precio = precio
    producto.cantidad_en_stock = cantidad_en_stock
    producto.save

    return redirect('/')


def eliminarProducto(request,id):
    producto = Producto.objects.get(id=id)
    producto.delete()

    return redirect('/')
