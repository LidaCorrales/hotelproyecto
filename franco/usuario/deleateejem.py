import sqlite3
conec=sqlite3.connect('D:/cerberus/hotelproyecto/franco/usuario/cerberustest.db')
#D:\\cerberus\\hotelproyecto\\franco\\cerberus
curso=conec.cursor()
sentencia=f" DELETE FROM usuario WHERE id_usuario_usu = 17 AND id_tipo_usu = 2 ;"
curso.execute(sentencia) 
conec.commit()
curso.close