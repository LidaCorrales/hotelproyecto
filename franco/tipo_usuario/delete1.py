import sqlite3
conec=sqlite3.connect('D:/cerberus/hotelproyecto/franco/usuario/cerberustest.db')
#D:\\cerberus\\hotelproyecto\\franco\\cerberus
curso=conec.cursor()

def borrar(tabla,columna,dato1,):
    sentencia=f" DELETE FROM {tabla} WHERE {columna} = {dato1}  ;"
    curso.execute(sentencia) 
    conec.commit()
    curso.close

"""borrar('usuario','id_usuario_usu',22)"""