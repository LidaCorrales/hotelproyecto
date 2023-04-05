import sqlite3
conec=sqlite3.connect('D:/cerberus/hotelproyecto/franco/usuario/cerberustest.db')
#D:\\cerberus\\hotelproyecto\\franco\\cerberus
curso=conec.cursor()

def borrar(tabla,columna,dato1,columna2,dato2):
    sentencia=f" DELETE FROM {tabla} WHERE {columna} = {dato1} AND {columna2} = '{dato2}' ;"
    curso.execute(sentencia) 
    conec.commit()
    curso.close

borrar('usuario','id_usuario_usu',20,'nombre_usu','franco')