import math

lista_funciones = dir(math)
archivo = open("funciones_math.txt", "w")
for funcion in lista_funciones:
    print(funcion)
    archivo.write(funcion + "\n")