from random import choice

opciones = ["cara", "cruz"]

for i in range(5):
    print(f"Tirada {i+1}: {choice(opciones)}")
