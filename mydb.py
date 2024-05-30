import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root', #User from MySQL
	passwd = '1234' #Password from MySQL
	)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE Baza_Danych")
