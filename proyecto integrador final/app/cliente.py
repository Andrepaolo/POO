from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import sqlite3
from reportlab.pdfgen import canvas
from  cliente_pdf import *
from tkdocviewer import *
class Cliente:
    db = "basedata.db"

    def __init__(self, window):
        self.window = window
        self.window.geometry("1000x800")
        self.window.iconbitmap("7_97254.ico")
        self.window.title("Clientes")
        self.Color=("blue")

        frame = LabelFrame(self.window, text="Cliente")
        frame.grid(row=0, column=0, columnspan=3, pady=20)

        ttk.Button(frame, text="Nuevo", command=self.new_cliente).grid(row=0, column=0)
        frame_options = LabelFrame(frame, text="Opciones")
        frame_options.grid(row=0, column=0, sticky = W + E)
        ttk.Button(frame_options, text="Nuevo", command=self.new_cliente).grid(row=0, column=0, sticky = W + E)
        ttk.Button(frame_options, text="Editar", command=self.edit).grid(row=0, column=1, sticky = W + E)
        ttk.Button(frame_options, text="Eliminar", command=self.delete).grid(row=0, column=2, sticky = W + E)
        ttk.Button(frame_options, text="Cerrar", command=self.close).grid(row=0, column=3, sticky = W + E)
        ttk.Button(frame_options, text="Pdf", command=self.pdf).grid(row=0, column=4, sticky = W + E)
        # tabla
        self.table = ttk.Treeview(frame, height=20,  columns=("name", "customer_type","direction","telephone"))
        self.table.grid(row=4, column=0)
        self.table.heading('#0', text='ID')
        self.table.heading('name', text='Nombre')
        self.table.heading('customer_type', text='Tipo de cliente')
        self.table.heading('direction', text='Direcion')
        self.table.heading('telephone', text='Telefono')
    
        self.get_clientes()

    def pdf(self):
        query = 'SELECT * FROM cliente'
        rows = self.query(query)
        list=[];
        file_name="clientes.pdf"
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

    def new_cliente(self):
        self.new_window = Toplevel()
        self.new_window.title = 'Nuevo Cliente'
        self.new_window.iconbitmap("7_97254.ico")
        Label(self.new_window, text = 'Direccion:').grid(row = 0, column = 1)
        direction = Entry(self.new_window)
        direction.grid(row = 0, column = 2)
        Label(self.new_window, text = 'Nombre:').grid(row = 1, column = 1)
        name = Entry(self.new_window)
        name.grid(row = 1, column = 2)
        Label(self.new_window, text = 'Tipo de cliente:').grid(row = 2, column = 1)
        customer_pyte= Entry(self.new_window)
        customer_pyte.grid(row = 2, column = 2)
        Label(self.new_window, text = 'Telefono:').grid(row = 3, column = 1)
        telephone= Entry(self.new_window)
        telephone.grid(row = 3, column = 2)
        Button(self.new_window, text = 'Guardar', command = lambda: self.save_cliente(name.get(),  customer_pyte.get(), direction.get(),telephone.get() )).grid(row = 5, column = 2, sticky = W)
        self.new_window.mainloop()

    def query(self, query, params=()):
        with sqlite3.connect(self.db) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, params)
            conn.commit()
        return result

    def get_clientes(self):
        list = self.table.get_children()
        for item in list:
            self.table.delete(item)        

        query = 'SELECT * FROM cliente'
        rows = self.query(query)
        for row in rows:
            self.table.insert(parent='', index=row[0], iid=row[0], text=row[0], values=(row[1], row[2], row[3], row[4]))

    def save_cliente(self, name, customer_type, direction,telephone):
        query = 'INSERT INTO cliente VALUES(NULL,?,?,?,?)'
        params = (name, customer_type, direction,telephone)
        self.query(query, params)
        self.new_window.destroy()
        self.get_clientes()

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
        query = 'DELETE FROM cliente WHERE id=?'
        self.query(query, (id,))
        self.get_clientes()
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
        old_customer_type = self.table.item(self.table.selection())['values'][1]
        old_direction = self.table.item(self.table.selection())['values'][2]
        old_telephone = self.table.item(self.table.selection())['values'][3]

        self.edit_window = Toplevel()
        self.edit_window.title = 'Edit Cliente'
        self.edit_window.iconbitmap("7_97254.ico")
        # Nombre Anterior
        Label(self.edit_window, text = 'Nombre Anterior:').grid(row = 0, column = 1)
        Entry(self.edit_window, textvariable = StringVar(self.edit_window, value = name), state = 'readonly').grid(row = 0, column = 2)
        # Nuevo Nombre
        Label(self.edit_window, text = 'Nuevo Nombre:').grid(row = 1, column = 1)
        new_name = Entry(self.edit_window, textvariable=name)
        new_name.grid(row = 1, column = 2)
        
        # Tipo de cliente Anterior 
        Label(self.edit_window, text = 'Tipo de cliente Anterior:').grid(row = 2, column = 1)
        Entry(self.edit_window, textvariable = StringVar(self.edit_window, value = old_customer_type), state = 'readonly').grid(row = 2, column = 2)
        # Nuevo Tipo de cliente
        Label(self.edit_window, text = 'Nuevo Tipo de cliente:').grid(row = 3, column = 1)
        new_customer_type= Entry(self.edit_window)
        new_customer_type.grid(row = 3, column = 2)
        
        # Direccion Anterior 
        Label(self.edit_window, text = 'Direccion Anterior:').grid(row = 4, column = 1)
        Entry(self.edit_window, textvariable = StringVar(self.edit_window, value = old_direction), state = 'readonly').grid(row = 4, column = 2)
        # Nueva Direccion
        Label(self.edit_window, text = 'Nueva Direccion:').grid(row = 5, column = 1)
        new_direction= Entry(self.edit_window)
        new_direction.grid(row = 5, column = 2)

        # telefono Anterior 
        Label(self.edit_window, text = 'Telefono Anterior:').grid(row = 6, column = 1)
        Entry(self.edit_window, textvariable = StringVar(self.edit_window, value = old_telephone), state = 'readonly').grid(row = 6, column = 2)
        # Nuevo telefono
        Label(self.edit_window, text = 'Nuevo Telefono:').grid(row = 7, column = 1)
        new_telephone= Entry(self.edit_window)
        new_telephone.grid(row = 7, column = 2)



        Button(self.edit_window, text = 'Actualizar', command = lambda: self.edit_records(id, new_name.get(), new_customer_type.get(),  new_direction.get(), new_telephone.get())).grid(row = 8, column = 2, sticky = W)
        self.edit_window.mainloop()
        
    def edit_records(self, id,new_name,  new_customer_type, new_direction, new_telephone):
        query = 'UPDATE cliente SET name = ?, customer_type = ?, direction = ?,telephone = ? WHERE id= ?'
        parameters = (new_name, new_customer_type,new_direction,new_telephone, id)
        self.query(query, parameters)
        self.edit_window.destroy()
        self.get_clientes()