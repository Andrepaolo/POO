from tkinter import*
from tkinter.ttk import *


index=Tk()
index.title("Login")
index.geometry("300x150")
index.iconbitmap("7_97254.ico")
index.config(bg="#2DD1EC")
index.resizable(width=False, height=False)

lusu=Label(index, text="Ingresar Usuario: ")
lusu.pack()

user=StringVar()
euse=Entry(index, width=30, textvariable=user)
euse.pack()

ipas=Label(index, text="contraseña: ")
ipas.pack()

pas=StringVar()
epas=Entry(index, width=30, show="*", textvariable=pas)
epas.pack()

def ingresar():
    if user.get()=="12345" and pas.get()=="12345" :
        index.destroy()
    else:
        index.title("incorrecto")

bi=Button(index, text="Entrar", command=ingresar)
bi.pack()

index.mainloop()
