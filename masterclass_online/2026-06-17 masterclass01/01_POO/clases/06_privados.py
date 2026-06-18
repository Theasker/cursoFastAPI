class Perro:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print('Guau!')

    @classmethod
    def factory(cls):
        return cls("Perro feliz", 4)
    
Perro.habla()
perro1 = Perro("Andres", 2)
perro2 = Perro("Juan", 3)
perro3 = Perro.factory()
print(perro1.nombre)
print(perro2.nombre)
print(perro3.nombre, perro3.edad)