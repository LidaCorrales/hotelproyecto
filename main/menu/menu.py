from sys import path as ruta

ruta.append("C:\\Corrales\\hotelproyecto\\main")
import CRUD_reserva.insertar as CI
import CRUD_reserva.actualizar as CA
import CRUD_reserva.leer as CL
import CRUD_reserva.eliminar as CE

try:
    while True:
        print("Menu de reserva \nPresione 1 para acceder a datos de reserva")
        ctrl=int(input(' '))
        match ctrl:
            case 1:
                while True:
                    ctrl2=int(input("Seleccione 1 si desea crear una reserva \nSeleccione 2 si desea actualizar datos de reserva \nSeleccione 3 si desea leer datos de reserva \nSeleccione 4 si desea eliminar una reserva \nSeleccione 5 si desea acceder al menu principal \nSeleccione 0 para terminar"))
                    match ctrl2:
                        case 1:
                            CI.add()
                        case 2:
                            CA.actualizar()
                        case 3:
                            CL.leer()
                        case 4:
                            CE.eliminar()
                        case 5:
                            break
            case 0:
                break
except (TypeError, ValueError) as e:
    print(type(e), e)