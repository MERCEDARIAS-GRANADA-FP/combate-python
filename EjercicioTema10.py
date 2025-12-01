
#  APARTADO 1: CLASE BASE — CRIATURA

from abc import ABC, abstractmethod
import random
import copy

class Criatura(ABC):
    def __init__(self, nombre, planeta_origen):
        self.nombre = nombre
        self.planeta_origen = planeta_origen
        self.nivel = 1
        self.__energia = 100           # Atributo privado
        self.habilidades = []          # Lista de habilidades
        self.ko = False                # Estado KO
    # ENCAPSULACIÓN
    def get_energia(self):
        return self.__energia

    def set_energia(self, valor):
        self.__energia = max(0, min(100, valor))
        if self.__energia == 0:
            self.ko = True

    #  MÉTODOS BÁSICOS
    @abstractmethod
    def hacer_sonido(self):
        pass

    def usar_habilidad(self, habilidad):
        if self.ko:
            print(f"{self.nombre} está en KO y no puede usar habilidades.")
            return

        if habilidad not in self.habilidades:
            print(f"{self.nombre} no tiene la habilidad {habilidad}.")
            return

        print(f"{self.nombre} usa la habilidad {habilidad}!")
        self.set_energia(self.get_energia() - 20)

        if self.get_energia() == 0:
            print(f"{self.nombre} ha quedado en KO.")

    def recargar_energia(self):
        print(f"{self.nombre} está recargando energía...")
        self.set_energia(100)
        self.ko = False

    #  POLIMORFISMO
    def atacar(self, objetivo):
        """Método común que cada hijo modificará."""
        if self.ko:
            print(f"{self.nombre} no puede atacar, está KO.")
            return

        print(f"{self.nombre} ataca a {objetivo.nombre} de forma genérica.")
        objetivo.set_energia(objetivo.get_energia() - 10)

    #  EVOLUCIÓN
    def evolucionar(self):
        print(f"{self.nombre} está evolucionando...")
        self.nivel += 1



#  APARTADO 2: CLASES HIJAS CON COMPORTAMIENTO ÚNICO

class DragonSolar(Criatura):
    def __init__(self, nombre, planeta_origen):
        super().__init__(nombre, planeta_origen)
        self.alas = True
        self.habilidades = ["Fuego Solar", "Garra Radiante"]

    def hacer_sonido(self):
        print(f"{self.nombre}: «ROARRRR brillanteee!»")

    def escupir_fuego(self, objetivo):
        print(f"{self.nombre} escupe un chorro de fuego solar a {objetivo.nombre}!")
        objetivo.set_energia(objetivo.get_energia() - 25)

    def atacar(self, objetivo):
        print(f"{self.nombre} realiza un ataque solar contra {objetivo.nombre}!")
        objetivo.set_energia(objetivo.get_energia() - 20)

    def evolucionar(self):
        super().evolucionar()
        print(f"{self.nombre} aumenta su brillo y sus alas se fortalecen.")


class BabosaToxica(Criatura):
    def __init__(self, nombre, planeta_origen):
        super().__init__(nombre, planeta_origen)
        self.toxicidad = 50
        self.habilidades = ["Baba Ácida", "Gas Tóxico"]

    def hacer_sonido(self):
        print(f"{self.nombre}: «GLU... GLU... gloop...»")

    def corroer(self, objetivo):
        print(f"{self.nombre} lanza baba corrosiva a {objetivo.nombre}!")
        objetivo.set_energia(objetivo.get_energia() - 15)

    def atacar(self, objetivo):
        print(f"{self.nombre} intoxica a {objetivo.nombre}!")
        objetivo.set_energia(objetivo.get_energia() - 12)

    def evolucionar(self):
        super().evolucionar()
        self.toxicidad += 20
        print(f"{self.nombre} ahora es más tóxica.")


class RobotOmega(Criatura):
    def __init__(self, nombre, planeta_origen):
        super().__init__(nombre, planeta_origen)
        self.nivel_IA = 1
        self.habilidades = ["Rayo Láser", "Hackeo"]

    def hacer_sonido(self):
        print(f"{self.nombre}: «BEEP BEEP... Sistema operativo activo.»")

    def hackear(self, objetivo):
        print(f"{self.nombre} intenta hackear a {objetivo.nombre}!")
        objetivo.set_energia(objetivo.get_energia() - 18)

    def atacar(self, objetivo):
        print(f"{self.nombre} dispara un rayo láser a {objetivo.nombre}!")
        objetivo.set_energia(objetivo.get_energia() - 22)

    def evolucionar(self):
        super().evolucionar()
        self.nivel_IA += 1
        print(f"{self.nombre} actualiza su IA a nivel {self.nivel_IA}.")



#  APARTADO 3: ARENA DE COMBATE


class ArenaDeCombate:
    def __init__(self):
        self.criaturas = []

    def registrar(self, criatura):
        self.criaturas.append(criatura)

    def enfrentar(self, c1, c2):
        print("\nCOMIENZA LA BATALLA !!")
        print(f"{c1.nombre} VS {c2.nombre}")

        turno = 0
        while c1.get_energia() > 0 and c2.get_energia() > 0:
            atacante = c1 if turno % 2 == 0 else c2
            defensor = c2 if turno % 2 == 0 else c1

            atacante.atacar(defensor)
            turno += 1

        ganador = c1 if c1.get_energia() > 0 else c2
        print(f"Ganador: {ganador.nombre}\n")
        return ganador



#  APARTADO 4: LABORATORIO DE CLONACIÓN


class Laboratorio:
    def __init__(self):
        self.contador_clones = 1

    def clonar(self, criatura):
        clon = copy.deepcopy(criatura)
        clon.nombre = f"{criatura.nombre}_Clone{self.contador_clones}"

        # Defecto aleatorio
        defecto = random.choice(["energia", "habilidad"])

        if defecto == "energia":
            clon.set_energia(50)
        else:
            if clon.habilidades:
                clon.habilidades = clon.habilidades[:1]

        self.contador_clones += 1
        print(f"Clon creado: {clon.nombre} con defecto {defecto}")
        return clon



#  APARTADO 5: SCRIPT FINAL — EJECUCIÓN COMPLETA

if __name__ == "__main__":
    # Crear criaturas
    d = DragonSolar("Pyro", "Solaria")
    b = BabosaToxica("Gloop", "Mucus-9")
    r = RobotOmega("OmegaX", "Andrómeda")

    # Evolucionarlas
    d.evolucionar()
    b.evolucionar()
    r.evolucionar()

    # Arena
    arena = ArenaDeCombate()
    arena.registrar(d)
    arena.registrar(b)
    arena.registrar(r)

    # Primera batalla
    ganador1 = arena.enfrentar(d, b)

    # Clonar
    laboratorio = Laboratorio()
    clon = laboratorio.clonar(ganador1)

    # Segunda batalla con el clon
    ganador2 = arena.enfrentar(clon, r)

    # Resultados finales
    print("RESULTADOS FINALES")
    for c in [d, b, r, clon]:
        print(f"{c.nombre} -> Nivel: {c.nivel}, Energía: {c.get_energia()}")
