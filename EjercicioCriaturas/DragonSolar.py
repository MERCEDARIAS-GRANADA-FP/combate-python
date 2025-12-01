from EjercicioCriaturas.Criatura import Criatura


class DragonSolar(Criatura):
    def __init__(self, nombre, planeta_origen, alas_longitud, log_func=print):
        super().__init__(nombre, planeta_origen, ["Escupir Fuego", "Vuelo de Sol"], log_func=log_func)
        self.alas_longitud = alas_longitud
        self.furia = 0

    def hacer_sonido(self):
        return f"[{self.nombre}] ruge: GRAAAW! (Alas: {self.alas_longitud}m)"

    def escupir_fuego(self, objetivo):
        if self.estado == "KO": return 0
        coste = self.usar_habilidad("Escupir Fuego")
        if coste > 0:
            dano = 15 + self.nivel * 3 + self.furia
            objetivo.energia -= dano
            self.furia += 5
            self.log(
                f"[{self.nombre}] lanza fuego infernal! {objetivo.nombre} recibe {dano} de daño. Furia actual: {self.furia}")
            return dano
        return 0

    def atacar(self, objetivo):
        return self.escupir_fuego(objetivo)

    def evolucionar(self):
        super().evolucionar()
        self.alas_longitud += 5
        self.furia = 10
        self.habilidades.append("Aura de Llama")
        self.log(f"[{self.nombre}] DRAGÓN EVOLUCIONA: Alas crecen a {self.alas_longitud}m. Furia inicial al máximo!")