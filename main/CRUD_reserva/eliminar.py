from sqlite3 import *
from sys import path as ruta

ruta.append("C:\\Corrales\\hotelproyecto\\main")
import clases_reserva.reserva as R

def eliminar():
    con=connect("C:\\Corrales\\sqlite-tools\\DB\\cerberustest.db")
    mycursordelete=con.cursor()
    cantidad_re=int(input("Ingrese la cantidad de habitaciones de reserva que quiere eliminar: "))
    numero_re=int(input("Ingrese el numero de personas que quiere eliminar en la reserva"))
    fecha_init=(input("Ingrese la fecha de inicio de reserva que quiere eliminar(formato yyyy-mm-dd): "))
    fecha_final=(input("Ingrese la fecha final de reserva que quiere eliminar (formato yyyy-mm-dd): "))
    mycursordelete.execute("delete from reserva where can_hab_re =? and num_per_re =? and fecha_ini_re =? and fecha_fin_re =?",(cantidad_re, numero_re,fecha_init,fecha_final))
    con.commit()
    con.close()

    #comentario