import selectcerberus2,insertcerberus,update1cerberus,delete1
from insertcerberus import insert
from selectcerberus2 import seleccion
from update1cerberus import update
from delete1 import borrar


while True:
    print('1-selec"buscar"')
    print('2-añadir dato')
    print('3-borrar')
    print('4-actualizar dato')
    print('5-salir')
    ctrl=int(input('Ingrese la opcion: '))
    match ctrl:
        case 1:
            print("SELECT * FROM {tabla} WHERE {campo} {operador} '{dato}'")
            print("los datos a llenar son los q esta dentro de las llaves")
            seleccion(input("ingrese tabla: "),input("ingrese columna: "),input("ingrese operador: "),input("ingrese id: "))
        case 2: 
            print("INSERT INTO {tabla} ({columna}) values ('{dato}')")
            print("los datos a llenar son los q esta dentro de las llaves")
            insert(input("ingrese tabla: "),input("ingrese columna: "),input("nuevo valor: "))
        case 3:
            print(" DELETE FROM {tabla} WHERE {columna} = {dato1} ")
            print("los datos a llenar son los q esta dentro de las llaves")
            borrar(input("ingrese tabla: "),input("ingrese columna: "),input("ingrese id a borrar: "))
        case 4:
            print("UPDATE {tabla} SET {nombrecolum} = '{nuevovalor}'  where {colum2}{operador}{dato};")
            print("los datos a llenar son los q esta dentro de las llaves")
            update(input("ingrese tabla: "),input("ingrese columna: "),input("ingrese nuevo valor: "),input("ingrese colmuna2: "),input("ingrese operador: "),input("ingrese dato a evaluar: "))
        case 5:
            break