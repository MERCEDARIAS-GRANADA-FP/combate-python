import csv
import string

contador = 0

with open("empleados.csv", "r", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        for celda in fila:
            celda = celda.lower().translate(str.maketrans('', '', string.punctuation))
            palabras = celda.split()
            contador += len(palabras)

print("En el CSV hay", contador, "palabras")
