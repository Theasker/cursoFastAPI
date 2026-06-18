class Perro:
    patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def habla(cls):
        print('Guau')

    # Factory Method
    @classmethod
    def factory(cls):
        return cls("Nombre perro factory", 4)

Perro.habla()
perro1 = Perro("nombre 1", 2)
perro2 = Perro("nombre 2", 3)
perro3 = Perro.factory()
print(perro1.nombre)
print(perro2.nombre)
print(perro3.nombre)