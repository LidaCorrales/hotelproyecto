import sqlite3

conec=sqlite3.connect('D:/cerberus/hotelproyecto/franco/usuario/cerberustest.db')
print(type(conec))
curso=conec.cursor()
consulta="INSERT INTO usuario VALUES (17,'jose maria','soler','solerfranco146@gmail.com','cr 15 b 33 b- 14 sur', 213123123, 2);"
curso.execute(consulta)
