
import tkinter
import tkinter as tk
from tkinter import *
from tkinter import font
from ventas import Ventas

from reportlab.lib.colors import Color
from contraseña import *
from product import *
from cliente import *
from ventas import *

root = Tk()
root.title("PERU-GAS")
root.iconbitmap("7_97254.ico")
root.geometry("800x500")
root.config(bg="#2DD1EC")

fondo=PhotoImage(file="botellom.gif")
lbl=Label(root,image=fondo).place(x=150, y=0)
def ingresar():
    windows_ingresar=Tk()
    ingresar_windows=ingresar(windows_ingresar)
    windows_ingresar.mainloop()
def product():
    window_product=Tk()
    product_window=Product(window_product)
    window_product.mainloop()
def cliente():
    window_cliente=Tk()
    cliente_window=Cliente(window_cliente)
    window_cliente.mainloop()
def venta():
    window_venta=Tk()
    venta_window=Ventas(window_venta)
    window_venta.mainloop()
# Menu 1
menu1 = Menu(root)
root.config(menu=menu1)
sub_menu = Menu(menu1)
menu1.add_cascade(menu=sub_menu, label="*Opciones*")
sub_menu.add_command(label="Productos", command=product)
sub_menu.add_command(label="Clientes",command=cliente)
sub_menu.add_command(label="Ventas", command=venta)
# Menu2


input_frame =tkinter.LabelFrame(root, text="↑↑↑↑↑Bienvenido, selecciona la accion que deseas realizar↑↑↑↑↑", font=("Cooper Black",18), width=1000, height=100)
input_frame.pack(padx=0, pady=10)

root.mainloop()
