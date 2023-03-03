import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()
sql = "INSERT INTO mammiferi (nome_proprio, razza, peso, età) VALUES (%s, %s, %s, %s)"
val=[
    ('gino', 'pastore tibetano', 90, 140),
    ('ippolito', 'ippopotamo', 4000, 70),
    ('fernando', 'ippogrifo', 400, 3),
    ('frodo', 'aquila', 6, 2)
]

mycursor.executemany(sql, val)

mydb.commit()