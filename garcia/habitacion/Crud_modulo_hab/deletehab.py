import sqlite3
conexion=sqlite3.connect("C:/Users/jeshu/OneDrive/Documentos/cerberus/hotelproyecto/garcia/habitacion/cerberustest.db")
cur=conexion.cursor()
def delete(tabla,columna,dato):
    sent=f"DELETE FROM {tabla} WHERE {columna}={dato};"
    cur.execute(sent)
    conexion.commit()
    cur.close

"""delete("habitacion","id_habitacion_H","25")"""