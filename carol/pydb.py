import sqlite3
con=sqlite3.connect('C:\\cerberus\\Yate\\sqlite-tools\\db\\cerberus.db')
#con=sqlite3.connect('pythonsqlite/pythondb.db')
print(type(con))
micursor=con.cursor()
print(type(micursor))


new_sql="SELECT * from usuario;"
micursor.execute(new_sql)
lista=micursor.fetchall()
for fila in lista:
    print(fila[0])
    print(fila[1])
    print(fila[2])
    print(fila[3])
    print('*'*50)