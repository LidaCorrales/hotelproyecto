import sqlite3

conec=sqlite3.connect('cerberus.db')
print(type(conec))
curso=conec.cursor()
consulta="SELECT nombre_usu , apellido_usu , tipo_usu FROM usuario INNER JOIN tipo_usuario WHERE id_tipo_usu = id_tipo  ;"
curso.execute(consulta)
test=curso.fetchall()
for fila in test:                                            
    print(fila[0])                                            
    print(fila[1])
    print(fila[2])                                                                                                                                 
    print('*'*50)                                                                  