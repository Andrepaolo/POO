import tkinter 
from tkinter import *
from product import *
from cliente import *
root =Tk()
root.title("PERÚ-GAS")
root.iconbitmap("gas.ico")
root.geometry("500x300")
#frame 
def product():
    window_product=Tk()
    product_window=Product(window_product)
    window_product.mainloop()
def cliente():
    window_cliente=Tk()
    cliente_window=Cliente(window_cliente)
    window_cliente.mainloop()

menu1 = Menu(root)
root.config(menu=menu1)
sub_menu = Menu(menu1)
menu1.add_cascade(menu=sub_menu, label="Opciones")
sub_menu.add_command(label="Productos",command=product )
sub_menu.add_command(label="Clientes",command=cliente)
sub_menu.add_command(label="Ventas")


input_frame =tkinter.LabelFrame(root, text="↑↑↑↑↑Bienvenido, selecciona la accion que deseas realizar↑↑↑↑↑", width=450, height=50)
input_frame.pack(padx=0, pady=10)



root.mainloop()