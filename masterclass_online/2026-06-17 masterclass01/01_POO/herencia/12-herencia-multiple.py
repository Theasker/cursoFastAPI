class Animal:
    def comer(self):
        print("Comiendo...")
    
    def pasear(self):
        print("Paseando animales...")

class Perro:
    def pasear(self):
        print("Paseando al perro...")

class Chanchito(Perro, Animal):
    def programar(self):
        print("Programando...")

chan = Chanchito()
chan.pasear()
chan.comer()
chan.programar()