import mysql.connector

mi_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Johnclave1230$",
    database="ecommerce")

mi_cursor = mi_db.cursor()

#sql = """ INSERT INTO cliente
#            (nombre, apellido)
#            VALUES ('Maria', 'Paredes') """

#mi_cursor.execute(sql)
#mi_db.commit()

mi_cursor.execute("SELECT * FROM cliente")
for reg in mi_cursor:
    print(reg)

mi_db.close()
