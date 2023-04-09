from sqlite3 import *
from sys import path as ruta

ruta.append("C:\\Corrales\\hotelproyecto\\main")
import clases_reserva.reserva as R

def leer():
    con=connect("C:\\Corrales\\sqlite-tools\\DB\\cerberustest.db")
    mycursorread=con.cursor()
    mycursorread.execute("select * from reserva")
    status=mycursorread.fetchall()
    print("Datos de la reserva en la base de datos: ")
    for fila in status:
        print(fila[0])
        print(fila[1])
        print(fila[2])
        print(fila[3])
        print("*"*50)
    con.commit()
    con.close()