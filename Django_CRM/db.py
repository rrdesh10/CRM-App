import mysql.connector

db = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    passwd = 'Newmysqldb',
)

cursorObject = db.cursor()

cursorObject.execute("CREATE DATABASE CRM_Databse")

print("Table created")