class Animal:
    def __init__(self, nombre, peso):
        self.nombre = nombre
        self.peso = peso
        
    def respirar(self):
        print(f'{self.nombre} está respirando')
        
    def comer(self, alimento):
        print(f'{self.nombre} está comiendo {alimento}')

class Perro(Animal): # Hereda de Animal
    def __init__(self, nombre, peso, raza):
        super().__init__(nombre, peso)
        self.raza = raza
        
    def ladrar(self):
        print(f'{self.nombre} está ladrando')

    def __str__(self):
        return (f"Perro {self.nombre} de raza {self.raza}")
        

lassie = Perro('lassie', 44, 'Labrador')
lassie.respirar()
lassie.comer('carne')
lassie.ladrar()
print(lassie.raza)
print(lassie)


    
        