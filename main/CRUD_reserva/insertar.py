from sqlite3 import *
from sys import path as ruta

ruta.append("C:\\Corrales\\hotelproyecto\\main")
import clases_reserva.reserva as R


def add():
    con=connect("C:\\Corrales\\sqlite-tools\\DB\\cerberustest.db")
    mycursor=con.cursor()
    can_habitacion=int(input("Ingresar habitaciones que quiere reservar: "))
    num_personas=int(input("Ingresar el numero de personas en la reserva:"))
    fechaentrada=input("Ingrese la fecha de comienzo de la reserva (Formato yyyy-mm-dd): ")
    fechasalida=input("Ingresar fecha de finalizacion de la reserva (Formato yyyy-mm-dd): ")
    out=R.Reserva(can_habitacion,num_personas,fechaentrada,fechasalida)
    añade=(out.getCan_hab(),out.getNumpersona(),out.getFechauno(),out.getFechados())
    mycursor.execute("insert into reserva (can_hab_re,num_per_re,fecha_ini_re,fecha_fin_re) values(?,?,?,?)", añade)
    con.commit()
    con.close()


    with open("C:\\Corrales\\hotelproyecto\\main\\Reporte.txt","a") as flujo:
        flujo.write("Cantidad de habitaciones de la reserva: " + str(can_habitacion) +
                    "\nNumero de personas en la reserva: " + str(num_personas) +
                    "\nFecha de entrada registrada en la reserva: " + str(fechaentrada) +
                    "\nFecha de salida registrada en la reserva: " + str(fechasalida) + 
                    "\n" + "*"*50 +
                    "\n")