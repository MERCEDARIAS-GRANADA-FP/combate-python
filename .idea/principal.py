import micalculadora as mic

a = int(input("Introduce un número"))
b = int(input("Introducec otro numero"))

print("Suma: " + str(mic.calcularSuma(a,b)))
print("Resta: " + str(mic.calcularResta(a,b)))
print("Multiplicacion: " + str(mic.calcularMultiplicacion(a,b)))
print("Division: " + str(mic.calcularDivision(a,b)))

