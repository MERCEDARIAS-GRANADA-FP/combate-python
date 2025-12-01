import sqlite3

conexion = sqlite3.connect("escuela.db")
cursor = conexion.cursor()

cursor.execute("INSERT INTO estudiantes (nombre, edad, nota) VALUES ('Ana López', 20, 8.5)")
cursor.execute("INSERT INTO estudiantes (nombre, edad, nota) VALUES ('Carlos Pérez', 22, 7.9)")
cursor.execute("INSERT INTO estudiantes (nombre, edad, nota) VALUES ('Lucía García', 19, 9.2)")

conexion.commit()
conexion.close()

print("Estudiantes introducidos con exito!.")
