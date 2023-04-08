import sqlite3
conec=sqlite3.connect('D:/cerberus/hotelproyecto/franco/usuario/cerberustest.db')
curso=conec.cursor()

def insert(tabla, columna,dato):
    sentencia=f"INSERT INTO {tabla} ({columna}) values ('{dato}')"
    curso.execute(sentencia)  
    n=curso.rowcount
    conec.commit()
    curso.close
    return n
"""insert('usuario','nombre_usu','franco')"""