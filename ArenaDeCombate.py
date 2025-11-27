import random

from DragonSolar import DragonSolar
from Humano import Humano
from Coche import Coche


Criaturas = [
    DragonSolar("Ramon", "Jete"),
    Coche("Miata", "Otivar"),
    Humano("JoseLuis", "Torremolinos"),
    DragonSolar("Josefino", "Namek"),
    Coche("Twingo", "Saturno"),
    Humano("Ezequiel", "Desconocido")
]

criatura1 = random.choice(Criaturas)
criatura2 = random.choice(Criaturas)

while(criatura2 == criatura1):
    criatura2 = random.choice(Criaturas)

print(f"Salen a luchar {criatura1.nombre} y {criatura2.nombre}")
criatura1.hacer_sonido()
criatura2.hacer_sonido()

ganador = criatura1 # por defecto

for i in range(50):
    criatura1.atacar(criatura2)
    criatura2.atacar(criatura1)
if(criatura1.puntos < criatura2.puntos):
    ganador = criatura2
elif(criatura1.puntos==criatura2.puntos):
    if(criatura1.get_energia() < criatura2.get_energia()):
        ganador = criatura2
    if(criatura1.get_energia() == criatura2.get_energia()):
        ganador = None
if(ganador == None):
    print("Ha ocurrido un empate.")
else:
    print(f"Ha ganado {ganador.nombre}.")
criatura1.puntos = 0
criatura2.puntos = 0

# copiamos al ganador

clon = ganador.copiar()
print(f"Se ha clonado a {ganador.nombre}, el clon tiene {clon.get_energia()} energía.")

clon.recargar_energia()
ganador.recargar_energia()

ganador2 = ganador

for i in range(50):
    clon.atacar(ganador)
    ganador.atacar(clon)
if(ganador.puntos < clon.puntos):
    ganador2 = clon
elif(ganador.puntos==clon.puntos):
    if(ganador.get_energia() < clon.get_energia()):
        ganador2 = clon
    if(ganador.get_energia() == clon.get_energia()):
        ganador2 = None
if(ganador2 == None):
    print("Ha ocurrido un empate.")
else:
    print(f"Ha ganado {ganador2.nombre}.")
print(f"Estadísticas finales:\n"
      f"{criatura1.nombre}, {criatura1.get_energia()}/{criatura1.get_max_energia()}HP, nivel {criatura1.nivel}\n"
      f"{criatura2.nombre}, {criatura2.get_energia()}/{criatura2.get_max_energia()}HP, nivel {criatura2.nivel}\n"
      f"{clon.nombre}, {clon.get_energia()}/{clon.get_max_energia()}HP, nivel {clon.nivel}\n")


