import sqlite3
from funciones import *

conn = sqlite3.connect('C:\\hotel\\hotelproyecto\\carol\\cerberustest.db')

while True:
    print("Seleccione una opción:")
    print("1 - Seleccionar ")
    print("2 - Modificar ")
    print("3 - Eliminar ")
    print("4 - Agregar ")
    print("5 - Salir")

    opcion = int(input("ingrese la opcion: "))

    match opcion:
        case 1:
            print("ingrese los suientes datos solicitados: ")
            seleccion(input("ingrese tabla: "),input("ingrese campo: "),input("ingrese operador: "),input("ingrese dato: "))
            print(seleccion)
            
        case 2:
            print("ingrese los suientes datos solicitados: ")
            modificar(input("ingrese tabla: "),input("ingrese campo: "),input("ingrese dato: "),input("ingrese id: "))
            print(modificar)

        case 3:
            print("ingrese los suientes datos solicitados: ")
            eliminar(input("ingrese tabla: "),input("ingrese campo: "),input("ingrese dato a borrar: "))
            print(eliminar)

        case 4:
            print("ingrese los suientes datos solicitados: ")
            insertar(input("ingrese tabla: "),input("ingrese id del servicio: "),input("cantidad: "),input("id tipo de servicio: "),input("id de factura: "))
            print(insertar)

        case 5:
            print("Adiós!")
            conn.close()
            exit()

        case _:
            print("Opción inválida")
