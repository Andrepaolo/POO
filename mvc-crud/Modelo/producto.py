from os import curdir
from sqlite3.dbapi2 import Cursor, DatabaseError
from tkinter.constants import CURRENT
import Conexion as conexion

conexion=conexion.connect()
database=conexion[0]
Cursor=conexion[1]

class Producto:
    #query que ejecuta la insercion de un producto en la base de datos
    def registrarProducto(self, nombre, precio):
        query = "INSERT INT producto VALUES(NULL, ?, ?)"
        producto=(nombre,precio)
        Cursor.execute(query,producto)
        database.commit()
        return Cursor.rowcount

    def mostrarProducto(sellf):
        Cursor.execute("SELECT * FROM producto ORDER BY precio_producto")
        lista =[]
        lista.append(Cursor.rowcount)
        return lista

    def eliminarProducto(self, nombre):
        Cursor.execute("DELETE FROM productos WHERE nombre_producto = "+""+ nombre +"")
        database.commit()
        return Cursor.rowcount

    def editarProductos(self, nombreAntiguo, nombre, precio):
        query = "UPDATE productos SET nombre_producto=?, precio_producto=? WHERE nomnbre_producto=?"
        producto = (nombre, precio, nombreAntiguo)
        database.commit()
        return Cursor.rowcount

class Ventas:
    pass
