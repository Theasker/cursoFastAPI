# https://rszalski.github.io/magicmethods/

class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f"Perro {self.nombre} y edad {self.edad}"
    
    def habla(self):
        print(f"{self.nombre} dice Guau")
        return
    
    def __del__(self):
        print(f"El perro {self.nombre} ha sido eliminado")

perro = Perro("Rocky", 5)
print(perro)

texto = str(perro)
print(texto)

