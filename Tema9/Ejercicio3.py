import sqlite3

conexion = sqlite3.connect("escuela.db")
cursor = conexion.cursor()

print("Todos los estudiantes:")
cursor.execute("SELECT * FROM estudiantes")
estudiantes = cursor.fetchall()

for estudiante in estudiantes:
    print(estudiante)

print("\nEstudiantes mayores de 20 años (nombre y nota):")
cursor.execute(      "SELECT nombre, nota FROM estudiantes WHERE edad > 20")
mayores = cursor.fetchall()

for nombre, nota in mayores:
    print(f"Nombre: {nombre} | Nota: {nota}")

conexion.close()
