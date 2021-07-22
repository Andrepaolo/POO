import sqlite3
from tkinter.constants import E

class Model():
    #atributos 
    def crear_conexion(base_datos):
        try:    
            conexion=sqlite3.connect(base_datos)
        except sqlite3.Error as error:
            print ('_Hay un error de conexion:', error)

    def mostrar_tabla(conexion):
        sql ="SELECT name FROM sqlite_master WHERE type='table';"
        cursor= conexion.cursor()
        cursor.execute(sql)
        tablas = cursor.fetchall()

        for t in tablas:
            print(t)
    def saludar (self):
        return  conexion 
conexion= crear_conexion('basedata.db')

     
    