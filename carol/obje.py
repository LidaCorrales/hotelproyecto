from servicios import *
import sqlite3
lista=[]
with sqlite3.connect('C:\\proyecto\\hotelproyecto\\carol\\cerberustest.db')as con:
    micursor=con.cursor()
    new_sql="SELECT *  from servicio"
    #print(micursor.execute(new_sql).fetchall())
    lista=micursor.execute(new_sql).fetchall()

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