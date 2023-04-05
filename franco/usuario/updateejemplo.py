import sqlite3
conec=sqlite3.connect('D:/cerberus/hotelproyecto/franco/usuario/cerberustest.db')
#D:\\cerberus\\hotelproyecto\\franco\\cerberus
curso=conec.cursor()


sentencia=f"UPDATE usuario SET nombre_usu = 'soler' WHERE id_usuario_usu = 17;"
#print(sentencia)
lista=curso.execute(sentencia) 