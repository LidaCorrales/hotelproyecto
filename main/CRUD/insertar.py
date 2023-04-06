from sqlite3 import *
from sys import path as ruta
from datetime import datetime

ruta.append("C:\\Corrales\\hotelproyecto\\main")
import clases.reserva as R

#Pedir reserva por documento= preguntar
def add():
    con=connect("C:\\Corrales\\sqlite-tools\\DB\\cerberustest.db")
    mycursor=con.cursor()
    can_habitacion=int(input("Ingresar habitaciones que quiere reservar: "))
    num_personas=int(input("Ingresar el numero de personas en la reserva:"))
    fechaentrada=int(datetime.strptime(input("Ingresar dia, mes y año de la reserva:")))
    fechasalida=int(datetime.strptime(input("Ingresar dia, mes y año de finalizacion de la reserva:")))
    t = fechaentrada - fechasalida
    print("Dias de estadia: ", t)
    out=R.Reserva(can_habitacion,num_personas,fechaentrada,fechasalida)
    añade=(out.getCan_hab(),out.getNumpersona(),out.getFechauno(),out.getFechados())
    mycursor.execute("insert into reserva values(?,?,?,?)", add)
    con.commit()
    con.close()

add()