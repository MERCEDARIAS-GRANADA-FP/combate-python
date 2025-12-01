import sqlite3

try:
    conexion = sqlite3.connect("escuela.db")
    cursor = conexion.cursor()
    cursor.execute("""
    CREATE TABLE estudiantes (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        edad INTEGER,
        nota REAL
    )
    """)
    conexion.commit()
    print("Tabla 'estudiantes' creada correctamente.")
except sqlite3.OperationalError:
    print("La tabla 'estudiantes' ya existe en la base de datos.")
finally:
    if conexion:
        conexion.close()
