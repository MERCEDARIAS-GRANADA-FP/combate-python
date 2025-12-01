import miCalculadora as mic

a = int(input("Introduce un número"))
b = int(input("Introducec otro numero"))

print("Suma: " + str(mic.sumar(a,b)))
print("Resta: " + str(mic.restar(a,b)))
print("Multiplicacion: " + str(mic.multiplicar(a,b)))
print("Division: " + str(mic.dividir(a,b)))

