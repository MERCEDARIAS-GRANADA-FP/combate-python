import sqlite3

conexion = sqlite3.connect("escuela.db")
cursor = conexion.cursor()

cursor.execute("UPDATE estudiantes SET nota = 9.8 WHERE id = 1")
cursor.execute("DELETE FROM estudiantes WHERE id = 2")

print("Tabla de estudiantes actualizada:")
cursor.execute("SELECT * FROM estudiantes")
estudiantes = cursor.fetchall()

for estudiante in estudiantes:
    print(estudiante)

conexion.commit()
conexion.close()
print("Cambios guardados y conexión cerrada correctamente.")
