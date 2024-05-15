# Install Mysql on your computer : https://dev.mysql.com/downloads/installer/

#pip install mysql-connector-python 

import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root', #User form MySQL
	passwd = '1234' #Password from MySQL
	)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE Baza Danych")
