import random


class ArenaDeCombate:
    def __init__(self, log_func=print):
        self.participantes = []
        self.log = log_func

    def registrar_criatura(self, criatura):
        self.participantes.append(criatura)
        self.log(f"[Arena] {criatura.nombre} ha sido registrado en la arena.")

    def enfrentar_aleatorio(self):
        if len(self.participantes) < 2:
            self.log("[Arena] Se necesitan al menos dos criaturas para un combate.")
            return None

        combatientes = random.sample(self.participantes, 2)
        criatura1 = combatientes[0]
        criatura2 = combatientes[1]

        self.log("\n--- INICIO DEL COMBATE ---")
        self.log(
            f"Luchadores: {criatura1.nombre} (Nv. {criatura1.nivel}) vs {criatura2.nombre} (Nv. {criatura2.nivel})")
        self.log("----------------------------")

        turno = 0
        while criatura1.estado != "KO" and criatura2.estado != "KO" and turno < 10:
            turno += 1
            self.log(f"\n--- TURNO {turno} ---")

            criatura1.atacar(criatura2)
            if criatura2.estado == "KO": break

            criatura2.atacar(criatura1)

        self.log("\n--- FIN DEL COMBATE ---")
        return self._determinar_ganador(criatura1, criatura2)

    def _determinar_ganador(self, c1, c2):
        if c1.estado == "KO" and c2.estado == "KO":
            return "Empate KO"
        elif c1.estado == "KO":
            c2.evolucionar()
            return c2
        elif c2.estado == "KO":
            c1.evolucionar()
            return c1

        puntuacion1 = c1.energia + c1.nivel * 10
        puntuacion2 = c2.energia + c2.nivel * 10

        if puntuacion1 > puntuacion2:
            self.log(f"[Arena] {c1.nombre} gana por puntos.")
            c1.evolucionar()
            return c1
        elif puntuacion2 > puntuacion1:
            self.log(f"[Arena] {c2.nombre} gana por puntos.")
            c2.evolucionar()
            return c2
        else:
            return "Empate por Puntos"