
import sqlite3
con=sqlite3.connect('C:\\hotel\\hotelproyecto\\carol\\cerberustest.db')
micursor=con.cursor()

def seleccion(tabla, campo, operador,dato):
    sentencia=f"SELECT * FROM {tabla} WHERE {campo}{operador}'{dato}'"
    #print(sentencia)
    lista=micursor.execute(sentencia)
    return lista.fetchall()

#print(seleccion('servicio','can_ser','>','12'))
#print(seleccion('tipo_servicio','precio_servi','>','10.000'))

def modificar(tabla,campo,dato,id):
    sentencia=f"UPDATE {tabla} SET {campo}='{dato}' WHERE id_servicio_ser={id}"
    #sentencia1=f"UPDATE {tabla} SET {campo}='{dato}' WHERE id_tipo_servicio_servi={id}"
    print(sentencia)
    #print(sentencia1)
    micursor.execute(sentencia)
    #micursor.execute(sentencia1)
    con.commit()
    print('Modificación Exitosa!!!!')

#modificar('servicio','id_servicio_ser',5,8)
#modificar('tipo_servicio','id_tipo_servicio_servi',4,5)

def eliminar(tabla,campo,dato):
    sentencia=f"DELETE FROM {tabla} WHERE {campo}='{dato}'"
    micursor.execute(sentencia)
    con.commit()
    print('Eliminación Exitosa!!!!')

#eliminar('servicio','id_servicio_ser',5)
#eliminar('tipo_servicio','id_tipo_servicio_servi',4)

def insertar(tabla,id,ct,ts,fs):
    sentencia=f"INSERT INTO {tabla} VALUES ('{id}','{ct}','{ts}','{fs}')"
    micursor.execute(sentencia)
    con.commit()
    print('Registro Creado!!!!')


#insertar('servicio',5,8,26,3)

def insertar(tabla,id,ts,ps):
    sentencia=f"INSERT INTO {tabla} VALUES ('{id}','{ts}','{ps}')"
    micursor.execute(sentencia)
    con.commit()
    print('Registro Creado!!!!')

#insertar('tipo_servicio',5,'spaa',30.000)
