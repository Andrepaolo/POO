from tkinter import ttk
from tkinter import *
import sqlite3


class Product:
    db = "database.db"

    def __init__(self, window):
        self.window = window
        self.window.geometry("800x800")
        self.window.title("Productos")
        # Creamos un frame
        frame = LabelFrame(self.window, text="Nuevo Registro")
        frame.grid(row=0, column=0, columnspan=3, pady=20)
        Label(frame, text="Name: ").grid(row=0, column=0)
        self.name = Entry(frame)
        self.name.grid(row=0, column=1)  #

        Label(frame, text="Price: ").grid(row=1, column=0)
        self.price = Entry(frame)
        self.price.grid(row=1, column=1)

        ttk.Button(frame, text="Guardar", command=self.save_product).grid(row=2, column=1)
        # tabla
        self.table = ttk.Treeview(frame, height=20, columns=2)
        self.table.grid(row=3, column=0)
        self.table.heading('#0', text='Nombre')
        self.table.heading('#1', text='Precio')

        ttk.Button(frame, text="Editar", command=self.edit).grid(row=4, column=0)
        ttk.Button(frame, text="Eliminar", command=self.delete).grid(row=4, column=1)
        ttk.Button(frame, text="Cerrar", command=self.close).grid(row=4, column=2)
        self.get_products()

    def query(self, query, params=()):
        with sqlite3.connect(self.db) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, params)
            conn.commit()
        return result

    def get_products(self):
        list = self.table.get_children()
        for item in list:
            self.table.delete(item)

        query = 'SELECT * FROM product'
        rows = self.query(query)
        for row in rows:
            self.table.insert('', 0, text=row[1], values=row[2])

    def save_product(self):
        query = 'INSERT INTO product VALUES(NULL,?,?)'
        params = (self.name.get(), self.price.get())
        self.query(query, params)
        self.get_products()

    def close(self):
        self.window.destroy()
        return None

    def delete(self):
        try:
            self.table.item(self.table.selection())['text'][0]
        except IndexError as e:
            print(e)
        name = self.table.item(self.table.selection())['text']
        query = 'DELETE FROM product WHERE name=?'
        self.query(query, (name,))
        self.get_products()

    def edit(self):
        print("aqui editar")
