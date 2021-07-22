from cliente import Cliente
from product import Product
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import sqlite3
from reportlab.pdfgen import canvas
from  venta_pdf import *
from tkdocviewer import *
class Ventas:
    db = "basedata.db"

    def __init__(self, window):
        self.window = window
        self.window.geometry("1000x500")
        self.window.iconbitmap("7_97254.ico")
        self.window.title("Vneta")
        
        # Creamos un frame
        frame = LabelFrame(self.window, text=" Venta")
        frame.grid(row=0, column=0, columnspan=3, pady=10)
        
        ttk.Button(frame, text="Nuevo", command=self.new_ventas).grid(row=0, column=0)
        frame_options = LabelFrame(frame, text="Opciones")
        frame_options.grid(row=0, column=0, sticky = W + E)
        ttk.Button(frame_options, text="Nuevo", command=self.new_ventas).grid(row=0, column=0, sticky = W + E)
        ttk.Button(frame_options, text="Editar", command=self.edit).grid(row=0, column=1, sticky = W + E)
        ttk.Button(frame_options, text="Eliminar", command=self.delete).grid(row=0, column=2, sticky = W + E)
        ttk.Button(frame_options, text="Cerrar", command=self.close).grid(row=0, column=3, sticky = W + E)
        ttk.Button(frame_options, text="Pdf", command=self.pdf).grid(row=0, column=4, sticky = W + E)
        # tabla
        self.table = ttk.Treeview(frame, height=20,  columns=("product","cliente", "precio","cantidad",))
        self.table.grid(row=5, column=0)
        self.table.heading('#0', text='ID')
        self.table.heading('product', text='producto')
        self.table.heading('cliente', text='cliente')
        self.table.heading('precio', text='precio')
        self.table.heading('cantidad', text='cantidad ')
   

        self.get_ventas()

    def pdf(self):
        query = 'SELECT * FROM ventas'
        rows = self.query(query)
        list=[];
        file_name="ventas.pdf"
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
        
    def new_ventas(self):
        self.new_window = Toplevel()
        self.new_window.title = 'Nuevo ventas'
        self.new_window.iconbitmap("7_97254.ico")
        Label(self.new_window, text = 'Tipo:').grid(row = 0, column = 1)
        producto = Entry(self.new_window)
        producto.grid(row = 0, column = 2)
        Label(self.new_window, text = 'Cliente').grid(row = 1, column = 1)
        precio= Entry(self.new_window)
        precio.grid(row = 1, column = 2)
        Label(self.new_window, text = 'Precio').grid(row = 2, column = 1)
        cantidad= Entry(self.new_window)
        cantidad.grid(row = 2, column = 2)
        Label(self.new_window, text = 'cantidad').grid(row = 3, column = 1)
        total= Entry(self.new_window)
        total.grid(row = 3, column = 2)
        Button(self.new_window, text = 'Guardar', command = lambda: self.save_ventas(producto.get(), precio.get(), cantidad.get(), total.get() )).grid(row = 5, column = 2, sticky = W)
        self.new_window.mainloop()
        
    def query(self, query, params=()):
        with sqlite3.connect(self.db) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, params)
            conn.commit()
        return result

    def get_ventas(self):
        list = self.table.get_children()
        for item in list:
            self.table.delete(item)

        query = 'SELECT * FROM ventas'
        rows = self.query(query)
        for row in rows:
            self.table.insert(parent='', index=row[0], iid=row[0], text=row[0], values=(row[1], row[2], row[3],row[4]))

    def save_ventas(self, cliente,product,precio,cantidad,total):
        query = 'INSERT INTO ventas VALUES(NULL,?,?,?,?)'
        params = (cliente,product,precio,cantidad,total)
        self.query(query, params)
        self.new_window.destroy()
        self.get_ventas()

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
        query = 'DELETE FROM ventas WHERE id=?'
        self.query(query, (id,))
        self.get_ventas()
        #messagebox.showinfo("showinfo", "Se elimino correctamente")
       
    def edit(self):
        print("aqui editar")
        try: 
             self.table.item(self.table.selection())['text']
        except IndexError as e:
            print("error")
            return
        id = self.table.item(self.table.selection())['text']
        product = self.table.item(self.table.selection())['values'][0]
        old_price = self.table.item(self.table.selection())['values'][1]
        old_cantidad = self.table.item(self.table.selection())['values'][2]
        old_total = self.table.item(self.table.selection())['values'][3]
     
        self.edit_window = Toplevel()
        self.edit_window.title = 'Edit venta'
        self.edit_window.iconbitmap("7_97254.ico")
        # Nombre Anteriorvarvah vcahdv ahdvhbjddhhdhdhdhdhhdhdhdhhdhdhhdhdhdhddhhdhdhdhd
        Label(self.edit_window, text = 'cliente Anterior:').grid(row = 0, column = 1)
        Entry(self.edit_window, textvariable = StringVar(self.edit_window, value = product), state = 'readonly').grid(row = 0, column = 2)
        # Nuevo Nombre
        Label(self.edit_window, text = 'Nuevo cliente:').grid(row = 1, column = 1)
        new_produc = Entry(self.edit_window, textvariable=product)
        new_produc.grid(row = 1, column = 2)
        
        # Precio Anterior 
        Label(self.edit_window, text = 'Prodcuto Anterior:').grid(row = 2, column = 1)
        Entry(self.edit_window, textvariable = StringVar(self.edit_window, value = old_price), state = 'readonly').grid(row = 2, column = 2)
        # Nuevo Precio
        Label(self.edit_window, text = 'Nuevo producto').grid(row = 3, column = 1)
        new_price= Entry(self.edit_window)
        new_price.grid(row = 3, column = 2)
        
        # Precio Anterior 
        Label(self.edit_window, text = 'precio Anterior:').grid(row = 4, column = 1)
        Entry(self.edit_window, textvariable = StringVar(self.edit_window, value = old_cantidad), state = 'readonly').grid(row = 4, column = 2)
        # Nuevo Precio
        Label(self.edit_window, text = 'precio nuevo:').grid(row = 5, column = 1)
        new_cantidad= Entry(self.edit_window)
        new_cantidad.grid(row = 5, column = 2)

        #Anterior Stock
        Label(self.edit_window, text = 'cantidad Anterior:').grid(row = 6, column = 1)
        Entry(self.edit_window, textvariable = StringVar(self.edit_window, value = old_total), state = 'readonly').grid(row = 6, column = 2)
        # Nuevo Stock
        Label(self.edit_window, text = 'nueva cantidad:').grid(row = 7, column = 1)
        new_total= Entry(self.edit_window)
        new_total.grid(row = 7, column = 2)


        
        Button(self.edit_window, text = 'Actualizar', command = lambda: self.edit_records(id, new_produc.get(), new_price.get(),  new_cantidad.get(), new_total.get())).grid(row = 8, column = 2, sticky = W)
        self.edit_window.mainloop()
        
    def edit_records(self, id,new_product, new_price,new_cantidad,new_total):
        query = 'UPDATE ventas SET product = ?, cliente = ?, precio = ?, cantidad =? = ? WHERE id= ?'
        parameters = (new_product, new_price,new_cantidad,new_total, id)
        self.query(query, parameters)
        self.edit_window.destroy()
        self.get_ventas()