from sqlite3 import *
from sys import path as ruta

ruta.append("C:\\Corrales\\hotelproyecto\\main")
import clases.reserva as R

#Pedir reserva por documento= preguntar
def add():
    con=connect("C:\\Corrales\\sqlite-tools\\DB\\cerberustest.db")
    mycursor=con.cursor()
    can_habitacion=int(input("Ingresar habitaciones que quiere reservar: "))
    num_personas=int(input("Ingresar el numero de personas en la reserva:"))
    fechaentrada=input("Ingrese la fecha de comienzo de la reserva (Formato yyyy-mm-dd): ")
    fechasalida=input("Ingresar fecha de finalizacion de la reserva (Formato yyyy-mm-dd): ")
    out=R.Reserva(can_habitacion,num_personas,fechaentrada,fechasalida)
    añade=(out.getCan_hab(),out.getNumpersona(),out.getFechauno(),out.getFechados())
    mycursor.execute("insert into reserva values(?,?,?,?)", add)
    con.commit()
    con.close()