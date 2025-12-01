import sqlite3
import pandas as pd

conexion = sqlite3.connect("escuela.db")

df = pd.read_sql_query("SELECT * FROM estudiantes", conexion)
print(df)

edad_media = df["edad"].mean()
print(f"Edad media de los estudiantes: {edad_media:.2f}")

conexion.close()
