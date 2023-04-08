import sqlite3
conexion=sqlite3.connect("C:/Users/jeshu/OneDrive/Documentos/cerberus/hotelproyecto/garcia/habitacion/cerberustest.db")
cur=conexion.cursor()
def  select(tabla,campo,operador,dato):
    sent=f"SELECT * FROM {tabla} WHERE {campo} {operador} '{dato}'"
    list=cur.execute(sent)
    list=cur.fetchall()
    for fila in list:
        print(fila)
        print("-"*50)
        
"""select("habitacion","id_habitacion_H","=","17")"""