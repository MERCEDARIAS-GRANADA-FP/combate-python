class Habilidad:
    nombre = str
    danio = int
    def __init__(self, nombre, danio):
        self.nombre = nombre
        self.danio = danio
    def get_nombre(self):
        return self.nombre
    def get_danio(self):
        return self.danio