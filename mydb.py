import mysql.connector 

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password123'
)

cursorObject = dataBase.cursor()

#create database
cursorObject.execute("CREATE DATABASE elderco")

print("All done!")