from Criatura import Criatura
from Habilidad import Habilidad


class Humano(Criatura):
    edad = 18
    habilidades = [
        Habilidad("Charla sobre economía", 15),
        Habilidad("Domesticar", 10)
    ]
    def __init__(self, nombre, planeta_origen):
        super().__init__(nombre, planeta_origen)

    def copiar(self):
        clon = super().copiar()
        clon.edad = self.edad
        clon.habilidades = self.habilidades
        return clon
    def hacer_sonido(self):
        print(f"{self.nombre} dice: Hola buenas tardes (sonido de humano)")
    def evolucionar(self):
        super().evolucionar()
        self.edad+=1