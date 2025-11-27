import random

class Criatura:
    nombre = str
    planeta_origen = str
    nivel = 1
    _energia = 100
    _max_energia = 100
    ko = False
    puntos = 0
    habilidades = []
    def __init__(self, nombre, planeta_origen):
        self.nombre = nombre
        self.planeta_origen = planeta_origen

    def hacer_sonido(self):
        pass
    def usar_habilidad(self, habilidad):
        if self.ko:
            self.ko = False
            self.recargar_energia()
            return None
        else:
            return self.habilidades[habilidad]
        pass # implementar seleccion de la lista
    def recargar_energia(self):
        print(f"{self.nombre} se cura")
        self._energia = self._max_energia
    def set_energia(self, energia):
        self._energia = energia
    def get_energia(self):
        return self._energia
    def get_max_energia(self):
        return self._max_energia
    def evolucionar(self):
        self.nivel+=1
        self._max_energia+=10
        print(f"¡{self.nombre} ha evolucionado a nivel {self.nivel}!")
    def atacar(self, objetivo):
        usada = self.usar_habilidad(random.randint(0,1))
        if(usada != None):
            if objetivo.get_energia() <= 0:
                print(f"{self.nombre} ataca a {objetivo.nombre}, pero el objetivo está debilitado")
            else:
                objetivo.set_energia(objetivo.get_energia() - usada.get_danio())
                if objetivo.get_energia() <= 0:
                    objetivo.ko = True
                    objetivo.set_energia(0)
                    print(f"{self.nombre} ataca a {objetivo.nombre} con {usada.get_nombre()}, su energia ahora es {objetivo.get_energia()}")
                    self.evolucionar()
                    self.puntos+=1
                else:
                    print(f"{self.nombre} ataca a {objetivo.nombre} con {usada.get_nombre()}, su energia ahora es {objetivo.get_energia()}")
    def copiar(self):
        nombre = f"{self.nombre}_CloneX"
        clon = Criatura(nombre, self.planeta_origen)
        clon.nivel = self.nivel
        clon._max_energia = self._max_energia
        clon._energia = self._energia - random.randint(1,round(self._max_energia/2))
        clon.planeta_origen = self.planeta_origen
        return clon



