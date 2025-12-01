import sqlite3

conexion = sqlite3.connect("escuela.db")
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS estudiantes (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    edad INTEGER,
    nota REAL
    )
""")

conexion.commit()
conexion.close()
print("Base de datos y tabla 'estudiantes' creadas")