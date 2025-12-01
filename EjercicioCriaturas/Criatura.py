import random

class Criatura:
    def __init__(self, nombre, planeta_origen, habilidades, log_func=print):
        self.nombre = nombre
        self.planeta_origen = planeta_origen
        self.nivel = 1
        self.__energia = 100
        self.habilidades = habilidades
        self.estado = "LISTO"
        self.log = log_func


    @property
    def energia(self):
        return self.__energia

    @energia.setter
    def energia(self, valor):
        if self.estado == "KO":
            self.log(f"[{self.nombre}] Advertencia: está en KO y no puede modificar energía.")
            return

        valor_nuevo = max(0, min(100, valor))
        self.__energia = valor_nuevo

        if self.__energia == 0:
            self.estado = "KO"
            self.log(f"[{self.nombre}] ha caído en KO. ¡Necesita recargar!")
        elif self.__energia > 0 and self.estado == "KO":
            self.estado = "LISTO"
            self.log(f"[{self.nombre}] ha salido del estado KO.")


    def hacer_sonido(self):
        raise NotImplementedError("El método hacer_sonido debe ser implementado por la subclase.")

    def usar_habilidad(self, habilidad_nombre):
        if self.estado == "KO":
            self.log(f"[{self.nombre}] no puede usar habilidades. Está en KO.")
            return 0

        if habilidad_nombre not in self.habilidades:
            self.log(f"[{self.nombre}] no conoce la habilidad {habilidad_nombre}.")
            return 0

        coste = 10 + self.nivel * 2

        if self.energia < coste:
            self.log(
                f"[{self.nombre}] no tiene suficiente energía para usar {habilidad_nombre}. ({self.energia}/{coste})")
            return 0

        self.energia -= coste
        self.log(f"[{self.nombre}] usa {habilidad_nombre} (-{coste} energía). Energía restante: {self.energia}")
        return coste

    def recargar_energia(self):
        self.estado = "LISTO"
        self.energia = 100
        self.log(f"[{self.nombre}] ha recargado completamente. Energía: {self.energia}")

    def evolucionar(self):
        self.nivel += 1
        self.log(f"[{self.nombre}] ha subido al Nivel {self.nivel}.")

    # --- Polimorfismo Obligatorio ---
    def atacar(self, objetivo):
        if self.estado == "KO":
            self.log(f"[{self.nombre}] no puede atacar. Está en KO.")
            return 0

        coste = self.usar_habilidad(random.choice(self.habilidades))
        if coste > 0:
            dano_base = self.nivel * 5
            objetivo.energia -= dano_base
            self.log(
                f"[{self.nombre}] ataca. {objetivo.nombre} recibe {dano_base} de daño. Energía de {objetivo.nombre}: {objetivo.energia}")
            return dano_base
        return 0

    def mostrar_stats(self):
        self.log(f"--- {self.nombre} ---")
        self.log(f"Nivel: {self.nivel} | Origen: {self.planeta_origen}")
        self.log(f"Energía: {self.energia} | Estado: {self.estado}")
        self.log(f"Habilidades: {', '.join(self.habilidades)}")