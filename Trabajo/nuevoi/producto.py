from tkinter import ttk
from tkinter import *
from Modelo import Producto


class VentanaProducto:
    def __init__(self, ventana):
        global mP
        mP = Producto.Producto()
        self.ventana = ventana
        self.ventana.title("Registro de productos")
        self.ventana.geometry("500x500")
        self.ventana.resizable(0,0)
        self.contenedor = LabelFrame(self.ventana, text="Ingresar nuevo producto")
        self.contenedor.grid(row = 0, column = 0, columnspan=3, padx = 20, pady = 20)

        Label(self.contenedor, text="Nombre: ").grid(row=1, column=0)
        self.nombre = Entry(self.contenedor)
        self.nombre.focus()
        self.nombre.grid(row=1, column=1, padx=5)

        Label(self.contenedor, text="Precio: ").grid(row=2, column=0)
        self.precio = Entry(self.contenedor)
        self.nombre.focus()
        self.nombre.grid(row=2, column=1, padx=5)
        self.mensaje = Label(text='', fg = 'red')
        self.mensaje.grid(row = 3, column=0, columnspan=2, sticky= W + E )

        # tablas
        self.tabla = ttk.Treeview(height = 10, column = 2)
        self.tabla.grid(row = 4, column = 0, columnspan= 2, padx = 50)
        self.tabla.heading('#0', text = "Nombre", anchor = CENTER)
        self.tabla.heading('#1', text = "Precio", anchor = CENTER)

    def obtenerDatos(self):
        self.limpiarTabla()

        mostrar = mP.mostrarProducto()

        for producto in mostrar[1]:
            self.tabla.insert('', 0, text = producto[1], value = producto[2])

            if (mostrar[0]>0):
                self.tabla.insert('', 0, text = producto[1], values = producto[2])

    def limpiarTabla(self):
        registros = self.tabla.get_children()
        for dato in registros:
            self.tabla.delete(dato)





