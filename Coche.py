from Criatura import Criatura
from Habilidad import Habilidad


class Coche(Criatura):
    itv = False
    habilidades = [
        Habilidad("Quemar rueda", 15),
        Habilidad("Atropellar", 10)
    ]
    def __init__(self, nombre, planeta_origen):
        super().__init__(nombre, planeta_origen)

    def copiar(self):
        clon = super().copiar()
        clon.itv = self.itv
        clon.habilidades = self.habilidades
        return clon

    def hacer_sonido(self):
        print(f"{self.nombre} dice: BRRRoooom BRRRoooom Tutututututu (sonido de coche)")
    def evolucionar(self):
        super().evolucionar()
        self.nivel+=1
        if (self.nivel>5):
            itv = True
            print(f"Ahora {self.nombre} pasa la ITV")