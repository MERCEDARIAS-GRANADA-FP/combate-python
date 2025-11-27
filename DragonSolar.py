from Criatura import Criatura
from Habilidad import Habilidad

class DragonSolar(Criatura):
    habilidades = [
        Habilidad("Escupe fuego", 15),
        Habilidad("Volar", 10)
    ]
    nivel_alas = 1

    def __init__(self, nombre, planeta_origen):
        super().__init__(nombre, planeta_origen)
    def copiar(self):
        clon = super().copiar()
        clon.habilidades = self.habilidades
        clon.nivel_alas = self.nivel_alas
        return clon

    def hacer_sonido(self):
        print(f"{self.nombre} dice: GGGRRRRrrrrooooooaaaaauuuugggghhh (sonido de dragón)")
    def evolucionar(self):
        super().evolucionar()
        self.nivel_alas+=1

