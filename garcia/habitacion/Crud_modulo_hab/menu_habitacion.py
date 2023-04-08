import selecthab, inserthab, updatehab, deletehab
from selecthab import select
from inserthab import insert
from deletehab import delete
from updatehab import update


while True:
    print("1-Busqueda")
    print("2-Añadir datos")
    print("3-Borrar datos")
    print("4-Actualizar")
    print("5-Salir")
    control=int(input("Ingresa la opción que desee:"))
    match control:
        case 1:
            print("Datos a consultar")
            print("Tablas pertenecientes a este modulo:")
            print("habitacion//tipo_habitacion//estado_hab")
            print("{Tabla}--{Columna}--{Dato}")
            select(input("Ingrese la  tabla:"),input("Ingrese la columna:"),"=",input("Ingrese el Id a consultar:"))
        case 2:
            print("Datos al insertar")
            print("Tablas pertenecientes a este modulo:")
            print("habitacion//tipo_habitacion//estado_hab")
            print(" {Tabla}--{Columna}--{Datos}")
            insert(input("Ingrese la  tabla:"),input("Ingrese  la columna:"),input("Añadir datos:"))
            print("-"*50)
        case 3:
            print("Datos a borrar")
            print("Tablas pertenecientes a este modulo:")
            print("habitacion//tipo_habitacion//estado_hab")
            print("{Tabla}--{Columna}--{Dato}")
            delete(input("Ingrese la  tabla:"),input("Ingrese la columna:"),input("Ingrese el dato a borrar:"))
            print("-"*50)
        case 4:
            print("Datos a actualizar")
            print("Tablas pertenecientes a este modulo:")
            print("habitacion//tipo_habitacion//estado_hab")
            print("{Tabla}--{Columna}--{Dato_nuevo}--{Columna_nueva}--{Dato}")
            update(input("Ingrese la  tabla:"),input("Ingrese la columna:"),input("Ingrese el dato nuevo:"),input("Ingrese la segunda columna:"),"=",input("Ingrese Id a actualizar:"))
            print("-"*50)
        case 5:
            print("A salido del menu")
            break
        