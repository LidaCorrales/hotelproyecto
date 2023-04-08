from servicios import *
from tipo_servicio import *
import sqlite3
lista=[]
lista2=[]
with sqlite3.connect('C:\\hotel\\hotelproyecto\\carol\\cerberustest.db')as con:
    micursor=con.cursor()
    new_sql="SELECT *  from servicio"
    new_sql2="SELECT *  from tipo_servicio"
    #print(micursor.execute(new_sql).fetchall())
    lista=micursor.execute(new_sql).fetchall()
    lista2=micursor.execute(new_sql2).fetchall()

servi=[]
for fila in lista:
    id_servicio_ser=fila[0]
    can_ser=fila[1]
    id_tp_ser=fila[2]
    id_factura=fila[3]
    ob=Servicios(id_servicio_ser,can_ser,id_tp_ser,id_factura)
    servi.append(ob)

print(servi)

for p in servi:
    print(p.getIdservi())
    #print("*******")
    #print(p.getcanser())

servi2=[]
for fila2 in lista2:
    id_tipo_servicio_servi=fila2[0]
    tipo_servi=fila2[1]
    precio_servi=fila2[2]
    ob2=tipo_servicio(id_tipo_servicio_servi,tipo_servi,precio_servi)
    servi2.append(ob2)

print(servi2)

for j in servi2:
    print(j.getIdtipservi())
    