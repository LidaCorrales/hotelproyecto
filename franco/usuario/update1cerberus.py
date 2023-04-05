import sqlite3

conec=sqlite3.connect('D:/cerberus/hotelproyecto/franco/usuario/cerberustest.db')
print(type(conec))
curso=conec.cursor()

def update(tabla,nombrecolum, nuevovalor,colum2,operador,dato):
    sentencia=f"UPDATE {tabla} SET {nombrecolum} = '{nuevovalor}'  where {colum2}{operador}{dato};"
    curso.execute(sentencia)
    n=curso.rowcount
    conec.commit()
    curso.close
    return n

print(update('usuario','nombre_usu','pinocho','id_usuario_usu','=',14))