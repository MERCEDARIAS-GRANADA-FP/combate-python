import random
import copy


class Laboratorio:
    def __init__(self, log_func=print):
        self.clones_registrados = 0
        self.log = log_func

    def clonar_criatura(self, original):
        self.clones_registrados += 1


        clon = copy.deepcopy(original)


        clon.nombre = f"{original.nombre}_Clone{self.clones_registrados}"


        clon.log = self.log


        defecto = random.choice(["Energia Reducida", "Habilidades Limitadas", "Nivel Bajo"])

        if defecto == "Energia Reducida":

            clon.energia = random.randint(10, 50)
            self.log(f"[LAB] CLON CREADO: {clon.nombre} | Defecto: Energía Inicial Reducida ({clon.energia})")

        elif defecto == "Habilidades Limitadas":

            if len(clon.habilidades) > 1:
                clon.habilidades = [random.choice(clon.habilidades)]
            clon.nivel = 1
            self.log(f"[LAB] CLON CREADO: {clon.nombre} | Defecto: Habilidades Limitadas (solo {clon.habilidades[0]})")

        else:

            clon.nivel = 1

            clon.habilidades = clon.habilidades[:1]
            self.log(f"[LAB] CLON CREADO: {clon.nombre} | Defecto: Retroceso de Nivel y Habilidades.")

        return clon