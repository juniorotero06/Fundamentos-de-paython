import mysql.connector

mi_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Johnclave1230$",
    database="ecommerce")

mi_cursor = mi_db.cursor()

sql = """ INSERT INTO cliente
            (nombre, apellido)
            VALUES (%s, %s) """

#valores = ("Mercedes", "Rojas")
#mi_cursor.execute(sql, valores)

valores = [("Carlos", "Parco"),
           ("Kyle", "Smith"),
           ("Anderson", "Salazar")]
mi_cursor.executemany(sql, valores)

mi_db.commit() ## Se debe ejecutar antes de que se cierra 
##la conexion a la bd para mandar los cambios si no, no se realizaran

mi_cursor.execute("SELECT * FROM cliente")
for reg in mi_cursor:
    print(reg)

mi_db.close()
