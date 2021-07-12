from tkinter import ttk
from tkinter import *
import tkinter.messagebox as tk
import sqlite3

conn = sqlite3.connect("basededatos.db")
cur = conn.cursor()

conn.execute("CREATE TABLE IF NOT EXISTS balance(empleado_id text, licencia_nefermedad int, licencia_maternidad int, licencia_emergnecia int)")
conn.execute("CREATE TABLE IF NOT EXISTS estado(licencia_id int, empelado_id int, licencia text, fecha_actual text, fecha1 text, dias int, estadot text, hrs_estado text)")
conn.execute("CREATE TABLE IF NOT EXISTS empleado(regsitro_id text, empleado_id text, password text, nombres text, numero_contacto text, empleado_mail text, empleado_direccion text)")

class AdminCLass:
    def AdminLogin(self):
        pass
    def adminwondow(self):
        pass
    def informacionEmpleado(self):
        pass
    def listadopermiso(self):
        pass
    def fecha_regristro(self):
        pass
    def licencia(self):
        pass

class EmpleadoClass:
    def empleadoLogin(self):
        pass
    def empleadoLoginWindow(self):
        pass
    def informacionEmpleadoWindow(self):
        pass
    def aplicacion(self):
        pass
    def balance(self):
        pass
    def windowBalance(self):
        pass
    def licenciaEmpleadoStado(self):
        pass
    def windowStado(self):
        pass
    def todosEmpleadoEstado(self):
        pass
    def empleadoLogout(self):
        pass

class RegistroClass:
    def regristro(self):
        pass

class actualizaClass:
    def actualizaInformacion(self):
        pass
    def actualizaWindow(self):
        pass
    def empleadoLogout(self):
        pass
    def informacionEmpleadoWindow(self):
        pass   
    def actualizarNombre(self):
        pass
    def actualizarDireccion(self):
        pass
    def actualizaEmail(self):
        pass
    def cambiaPassword(self):
        pass

class RHClass:
    def RHLogin(self):
        pass
    def listaLicencias(self):
        pass
    def licenciaAprobada(self):
        pass