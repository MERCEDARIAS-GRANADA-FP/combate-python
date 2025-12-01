import random

from EjercicioCriaturas.Criatura import Criatura


class RobotOmega(Criatura):
    def __init__(self, nombre, planeta_origen, nivel_ia, log_func=print):
        super().__init__(nombre, planeta_origen, ["Hackear", "Rayo Laser"], log_func=log_func)
        self.nivel_ia = nivel_ia
        self.escudo_activo = False

    def hacer_sonido(self):
        return f"[{self.nombre}] dice: *Bip, bop... IA Nivel: {self.nivel_ia}*"

    def activar_escudo(self):
        if self.estado == "KO": return
        if not self.escudo_activo:
            self.escudo_activo = True
            self.energia -= 5
            self.log(f"[{self.nombre}] activa un escudo de energía. (-5 energía)")
        else:
            self.log(f"[{self.nombre}] El escudo ya está activo.")

    def atacar(self, objetivo):
        if self.estado == "KO": return 0

        if random.random() < 0.2:
            self.log(f"[{self.nombre}] intenta hackear a {objetivo.nombre}...")
            if objetivo.energia > 10:
                objetivo.energia -= 10
                self.energia -= 5
                self.log(f"[Hackeo] exitoso! {objetivo.nombre} pierde 10 de energía.")
            return 10

        return super().atacar(objetivo)

    def evolucionar(self):
        super().evolucionar()
        self.nivel_ia += 2
        self.log(
            f"[{self.nombre}] ROBOT EVOLUCIONA: Nivel de IA incrementado a {self.nivel_ia}. Mayor probabilidad de éxito en hackeos.")