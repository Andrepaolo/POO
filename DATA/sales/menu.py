from tkinter import *
from product import *
root = Tk()
root.title("sistema de ventas")
root.geometry("300x300")
def product():
    window_product=Tk()
    product_window=Product(window_product)
    window_product.mainloop()
# Menu 1
menu1 = Menu(root)
root.config(menu=menu1)
sub_menu = Menu(menu1)
menu1.add_cascade(menu=sub_menu, label="Opciones")
sub_menu.add_command(label="Productos", command=product)
sub_menu.add_command(label="Clientes")
sub_menu.add_command(label="Ventas")
# Menu2
sub_menu2 = Menu(menu1)
menu1.add_cascade(menu=sub_menu2, label="Opcion 2")
sub_menu2.add_command(label="Opcion 1")
sub_menu2.add_command(label="Opcion 2")

root.mainloop()
