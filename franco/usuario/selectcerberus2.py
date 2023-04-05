import sqlite3
conec=sqlite3.connect('D:/cerberus/hotelproyecto/franco/usuario/cerberustest.db')
curso=conec.cursor()

def seleccion(tabla, campo, operador,dato):
    sentencia=f"SELECT * FROM {tabla} WHERE {campo} {operador} '{dato}'"
    #print(sentencia)
    lista=curso.execute(sentencia)    
    lista=curso.fetchall()
    for fila in lista:                                            
        print(fila)                                                                                                                                                                             
        print('*'*50)  

seleccion('usuario','id_usuario_usu','=','5')