import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE mammiferi (id INT AUTO_INCREMENT PRIMARY KEY, nome_proprio VARCHAR(355), razza VARCHAR(355), peso INT, età INT)")



