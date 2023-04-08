import sqlite3
conexion=sqlite3.connect("C:/Users/jeshu/OneDrive/Documentos/cerberus/hotelproyecto/garcia/habitacion/cerberustest.db")
cur=conexion.cursor()

def insert(tabla,columna,dato):
    sent=f"INSERT INTO {tabla} ({columna}) values ('{dato}')"
    cur.execute(sent)
    var=cur.rowcount
    conexion.commit()
    cur.close
    return var
"""insert("habitacion","descripcion_H","normal")"""