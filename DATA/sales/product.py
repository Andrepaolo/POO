from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import sqlite3
from reportlab.pdfgen import canvas
from  product_pdf import *
from tkdocviewer import *
class Product:
    db = "database.db"

    def __init__(self, window):
        self.window = window
        self.window.geometry("800x800")
        self.window.title("Productos")
        # Creamos un frame
        frame = LabelFrame(self.window, text="Productos")
        frame.grid(row=0, column=0, columnspan=3, pady=20)
        
        
        ttk.Button(frame, text="Nuevo", command=self.new_product).grid(row=0, column=0)
        frame_options = LabelFrame(frame, text="Opciones")
        frame_options.grid(row=0, column=0, sticky = W + E)
        ttk.Button(frame_options, text="Nuevo", command=self.new_product).grid(row=0, column=0, sticky = W + E)
        ttk.Button(frame_options, text="Editar", command=self.edit).grid(row=0, column=1, sticky = W + E)
        ttk.Button(frame_options, text="Eliminar", command=self.delete).grid(row=0, column=2, sticky = W + E)
        ttk.Button(frame_options, text="Cerrar", command=self.close).grid(row=0, column=3, sticky = W + E)
        ttk.Button(frame_options, text="Pdf", command=self.pdf).grid(row=0, column=4, sticky = W + E)
        # tabla
        self.table = ttk.Treeview(frame, height=20,  columns=("name", "price","code"))
        self.table.grid(row=4, column=0)
        self.table.heading('#0', text='ID')
        self.table.heading('name', text='Nombre')
        self.table.heading('price', text='Precio')
        self.table.heading('code', text='codigo')
    
        self.get_products()

    def pdf(self):
        query = 'SELECT * FROM product'
        rows = self.query(query)
        list=[];
        file_name="productos.pdf"
        for row in rows:
            list.append(row)
        ReportPdf(list,file_name)
        # Create una pantalla
        pdf_window = Toplevel()
        # Instancia DocViewer 
        v = DocViewer(pdf_window)
        v.pack(side="top", expand=1, fill="both")
        # Display some document
        v.display_file(file_name)
        # Inicializa el evento 
        pdf_window.mainloop()
        
    def new_product(self):
        self.new_window = Toplevel()
        self.new_window.title = 'Nuevo Producto'
        Label(self.new_window, text = 'Codigo:').grid(row = 0, column = 1)
        code = Entry(self.new_window)
        code.grid(row = 0, column = 2)
        Label(self.new_window, text = 'Nombre:').grid(row = 1, column = 1)
        name = Entry(self.new_window)
        name.grid(row = 1, column = 2)
        Label(self.new_window, text = 'Precio:').grid(row = 2, column = 1)
        price= Entry(self.new_window)
        price.grid(row = 2, column = 2)
        Button(self.new_window, text = 'Guardar', 
        command = lambda: self.save_product(name.get(),  price.get(), code.get())).grid(row = 4, column = 2, sticky = W)
        self.new_window.mainloop()
        
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
            self.table.insert(parent='', index=row[0], iid=row[0], text=row[0], values=(row[1], row[2], row[3]))

    def save_product(self, name, price, code):
        query = 'INSERT INTO product VALUES(NULL,?,?,?)'
        params = (name, price, code)
        self.query(query, params)
        self.new_window.destroy()
        self.get_products()

    def close(self):
        self.window.destroy()
        return None

    def delete(self):
    
        try:
            self.table.item(self.table.selection())['text']
        except IndexError as e:
            print("error")
            #messagebox.showerror("Error", "Selecciona un producto para eliminar")
        id = self.table.item(self.table.selection())['text']
        query = 'DELETE FROM product WHERE id=?'
        self.query(query, (id,))
        self.get_products()
        #messagebox.showinfo("showinfo", "Se elimino correctamente")
       
    def edit(self):
        print("aqui editar")
        try: 
             self.table.item(self.table.selection())['text']
        except IndexError as e:
            print("error")
            return
        id = self.table.item(self.table.selection())['text']
        name = self.table.item(self.table.selection())['values'][0]
        old_price = self.table.item(self.table.selection())['values'][1]
        old_code = self.table.item(self.table.selection())['values'][2]
        self.edit_window = Toplevel()
        self.edit_window.title = 'Edit Product'
        # Nombre Anterior
        Label(self.edit_window, text = 'Nombre Anterior:').grid(row = 0, column = 1)
        Entry(self.edit_window, textvariable = StringVar(self.edit_window, value = name), state = 'readonly').grid(row = 0, column = 2)
        # Nuevo Nombre
        Label(self.edit_window, text = 'Nuevo Nombre:').grid(row = 1, column = 1)
        new_name = Entry(self.edit_window, textvariable=name)
        new_name.grid(row = 1, column = 2)
        
        # Precio Anterior 
        Label(self.edit_window, text = 'Precio Anterior:').grid(row = 2, column = 1)
        Entry(self.edit_window, textvariable = StringVar(self.edit_window, value = old_price), state = 'readonly').grid(row = 2, column = 2)
        # Nuevo Precio
        Label(self.edit_window, text = 'Nuevo Precio:').grid(row = 3, column = 1)
        new_price= Entry(self.edit_window)
        new_price.grid(row = 3, column = 2)
        
        # Codigo Anterior 
        Label(self.edit_window, text = 'Codigo Anterior:').grid(row = 4, column = 1)
        Entry(self.edit_window, textvariable = StringVar(self.edit_window, value = old_code), state = 'readonly').grid(row = 4, column = 2)
        # Nuevo Codigo
        Label(self.edit_window, text = 'Nuevo Codigo:').grid(row = 5, column = 1)
        new_code= Entry(self.edit_window)
        new_code.grid(row = 5, column = 2)
        
        Button(self.edit_window, text = 'Actualiazar', command = lambda: self.edit_records(id, new_name.get(), new_price.get(), new_code.get())).grid(row = 6, column = 2, sticky = W)
        self.edit_window.mainloop()
        
    def edit_records(self, id,new_name,  new_price, new_code):
        query = 'UPDATE product SET name = ?, price = ?, code = ? WHERE id= ?'
        parameters = (new_name, new_price,new_code, id)
        self.query(query, parameters)
        self.edit_window.destroy()
        self.get_products()

