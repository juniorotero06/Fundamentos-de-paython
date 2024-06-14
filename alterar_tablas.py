import mysql.connector

mi_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Johnclave1230$",
    database="ecommerce")

mi_cursor = mi_db.cursor()

sql = """ ALTER TABLE cliente
            ADD cliente_id  INT  AUTO_INCREMENT  PRIMARY KEY """

mi_cursor.execute(sql)


mi_cursor.execute("DESCRIBE cliente")
for columnas in mi_cursor:
    print(columnas)

mi_db.close()
