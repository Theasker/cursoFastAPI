class Perro:
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.patas = 4

lassie = Perro('Lassie', 'Collie', 103)
print(lassie.nombre)
print(lassie.raza)
print(lassie.edad)