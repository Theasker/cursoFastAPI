class Perro:
    patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def habla(cls): # cls se refire a la clase misma
        print('Guau!')

    
Perro.habla()