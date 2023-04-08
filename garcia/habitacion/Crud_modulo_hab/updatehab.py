import sqlite3
conexion=sqlite3.connect("C:/Users/jeshu/OneDrive/Documentos/cerberus/hotelproyecto/garcia/habitacion/cerberustest.db")
cur=conexion.cursor()
def update(tabla,columna,datonuevo,columna2,operador,dato):
    sent=f"UPDATE {tabla} SET {columna}='{datonuevo}'  WHERE {columna2}{operador}{dato};"
    cur.execute(sent)
    var=cur.rowcount
    conexion.commit()
    cur.close
    return var
"""update("habitacion","descripcion_H","nueva","id_habitacion_H","=","23")"""