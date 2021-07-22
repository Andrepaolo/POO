from tkinter import tkk
from tkinter import *
from Modelo import producto
from Vista import producto 


class ControladorEditar:
    global mp
    mp =producto.producto()
    def editarProducto(self, nombre, NombreNuevo, PrecioNuevo):

        fila = mp.editarproducto(nombre, NombreNuevo, PrecioNuevo)
        if (fila>0):
            ventana = Tk()
            vP = producto.VentanaProducto(ventana)
        else:
            vP.mensaje['text'] = "no es posible editar"
        vP.obtenerDAtos()
        ventana.destroy()

        