
import sqlite3
con=sqlite3.connect('C:\\proyecto\\hotelproyecto\\carol\\cerberustest.db')
micursor=con.cursor()

def seleccion(tabla, campo, operador,dato):
    sentencia=f"SELECT * FROM {tabla} WHERE {campo}{operador}'{dato}'"
    #print(sentencia)
    lista=micursor.execute(sentencia)
    return lista.fetchall()

#print(seleccion('servicio','can_ser','>','12'))

def modificar(tabla,campo,dato,id):
    sentencia=f"UPDATE {tabla} SET {campo}='{dato}' WHERE id_servicio_ser={id}"
    print(sentencia)
    micursor.execute(sentencia)
    con.commit()
    print('Modificación Exitosa!!!!')

#modificar('servicio','id_servicio_ser',5,8)

def eliminar(tabla,campo,dato):
    sentencia=f"DELETE FROM {tabla} WHERE {campo}='{dato}'"
    micursor.execute(sentencia)
    con.commit()
    print('Eliminación Exitosa!!!!')

#eliminar('servicio','id_servicio_ser',5)

def insertar(tabla,id,ct,ts,fs):
    sentencia=f"INSERT INTO {tabla} VALUES ('{id}','{ct}','{ts}','{fs}')"
    micursor.execute(sentencia)
    con.commit()
    print('Registro Creado!!!!')

#insertar('servicio',5,8,26,3)
