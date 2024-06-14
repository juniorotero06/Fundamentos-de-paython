import mysql.connector

mi_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Johnclave1230$",
    database="ecommerce")

mi_cursor = mi_db.cursor()

#sql = """SELECT * FROM cliente"""

#sql = """ SELECT nombre, apellido FROM cliente """

#sql = """ SELECT nombre, apellido FROM cliente
#            WHERE nombre = 'Maria' """

sql = """ SELECT nombre, apellido FROM cliente
            WHERE nombre = %s """
            
## %s significa que va a obtener un valor desde afuera, por lo general en una tupla

valores = ("Pedro",)
mi_cursor.execute(sql, valores)



for reg in mi_cursor:
    print(reg)



mi_db.close()
