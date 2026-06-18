# ejemplo de polimorfismo

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def comer(self):
        print(f'{self.nombre} está comiendo')

class Perro(Animal):
    def __init__(self, nombre, patas):
        super().__init__(nombre)
        self.patas = patas
        
    def ladrar(self):
        print(f'{self.nombre} está ladrando')
        
    def comer(self):
        print(f'{self.nombre} está comiendo croquetas')

# Genera un ejemplo de polimorfismo
lassie = Perro('Lassie', 4)
lassie.comer()
lassie.ladrar()
lassie.comer()