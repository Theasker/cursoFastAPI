class Perro:
    def __init__(self, nombre):
        self.nombre = nombre

    # convierte la función en una propiedad
    # Sólo funciona para los getters
    @property
    def nombre(self):
        print("Pasando por el getter")
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        print("Pasando por el setter")
        if nombre.strip():
            self.__nombre = nombre
        return

perro = Perro("Cantito")
print(perro.nombre)