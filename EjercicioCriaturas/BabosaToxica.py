from EjercicioCriaturas.Criatura import Criatura


class BabosaToxica(Criatura):
    def __init__(self, nombre, planeta_origen, toxicidad, log_func=print):
        super().__init__(nombre, planeta_origen, ["Corroer", "Baba Lenta"], log_func=log_func)
        self.toxicidad = toxicidad

    def hacer_sonido(self):
        return f"[{self.nombre}] murmura: *Slurp, slurp...* (Toxicidad: {self.toxicidad}%)"

    def corroer(self, objetivo):
        if self.estado == "KO": return 0
        coste = self.usar_habilidad("Corroer")
        if coste > 0:
            dano_toxico = 10 + self.toxicidad / 10
            objetivo.energia -= dano_toxico
            self.toxicidad += 10
            self.log(
                f"[{self.nombre}] corroe con ácido. {objetivo.nombre} recibe {dano_toxico} de daño. Toxicidad: {self.toxicidad}%")
            return dano_toxico
        return 0

    def atacar(self, objetivo):
        return self.corroer(objetivo)

    def evolucionar(self):
        super().evolucionar()
        self.toxicidad += 50
        if self.nivel >= 3:
            self.habilidades.append("Regeneracion")
        self.log(f"[{self.nombre}] BABOSA EVOLUCIONA: Toxicidad extrema. Capacidad de auto-curación mejorada.")