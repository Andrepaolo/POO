import sqlite3
from sqlite3.dbapi2 import Cursor

def connect():
    database = sqlite3.connect("producto.db")
    cursor = database.cursor()

    database.execute("CREATE TABLE IF NOT EXISTS productos(id_producto INT AUTO_INCREMENT NOT NULL, nombre_producto VARCHAR(50), precio_producto INT NOT NULL, CONSTRAINT pk_producto PRIMARY KEY(id_producto)) ")
    return [database, cursor]