from sqlite3 import *
from sys import path as ruta

ruta.append("C:\\Corrales\\hotelproyecto\\main")
import clases.reserva as R

def actualizar():
    while True:
        con=connect("C:\\Corrales\\sqlite-tools\\DB\\cerberustest.db")
        mycursoractu=con.cursor()
        print("Seleccione la columna que desee actualizar \nSeleccione 1 para actualizar cantidad de habitaciones \nSelecciona 2 para actualizar cantidad de personas \n Selecciona 3 para actualizar fechas \n Seleccione 4 para salir")
        editar=(int(input(' ')))
        match editar:
            case 1:
                can_habitacion=int(input("Ingresar cambio de numero de habitaciones: "))
                reserva=int(input("Ahora ingrese el id de reserva de la cual va a hacer el cambio: "))
                mycursoractu.execute("update reserva set can_hab_re =? where id_reserva_re =?",(can_habitacion,reserva))
                con.commit()
                con.close()
            case 2:
                num_personas=int(input("Ingresar cambio de numero de personas en la reserva:"))
                reserva=int(input("Ahora ingrese el id de reserva de la cual va a hacer el cambio: "))
                mycursoractu.execute("update reserva set num_per_re =? where id_reserva_re =?",(num_personas,reserva))
                con.commit()
                con.close()
            case 3:
                fechaentrada=input("Ingrese la fecha de comienzo de la reserva (Formato yyyy-mm-dd): ")
                fechasalida=input("Ingrese la fecha de finalizacion de la reserva (Formato yyyy-mm-dd): ")
                reserva=int(input("Ahora ingrese el id de reserva de la cual va a hacer el cambio: "))
                mycursoractu.execute("update reserva set fecha_ini_re and fecha_fin_re =? where id_reserva_re =?",(fechaentrada,fechasalida,reserva))
            case 4:
                break