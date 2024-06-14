import mysql.connector

mi_db = mysql.connector.connect(
    host = "localhost",
    user="root",
    password="Jun315274291@")

mi_cursor = mi_db.cursor()

##sql = "CREATE DATABASE ecommerce"
##sql = "DROP DATABASE ecommerce"
sql = "SHOW DATABASES"

mi_cursor.execute(sql)

for item in mi_cursor:
    print(item)

mi_db.close()

## Para entraar a una bd es USE <nombre de la bd>
## PAra crear una tabla es CREATE TABLE cliente( nombre VARCHAR(255), ...)
## para ver la tablas ejecutamos SHOW TABLES
# Para borrar una tabla y evitar que el programa tire error si no existe
## DROP TABLE IF EXISTS <nombre_tabla>
