import tkinter 
from tkinter import Button, Entry, IntVar

root=tkinter.Tk()
root.title("APPolo")
root.geometry('500x500')
razon_social=Entry(root)
razon_social.grid(row=1, columnspan=6)
capturar_empresa=Button(root, text='capturar datos')
razon_social=Entry(root)
razon_social.grid(row=2, columnspan=6)
razon_social=Entry(root)
razon_social.grid(row=3, columnspan=6)
capturar_empresa.grid(row=4)
# capturar_empresa.grid(row=2)






root.mainloop()