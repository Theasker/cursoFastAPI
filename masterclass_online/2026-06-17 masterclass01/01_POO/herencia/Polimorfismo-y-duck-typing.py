# DuckTyping
class Pato:
    def graznar(self):
        print("¡Quack, quack!")

class PersonaDisfrazada:
    def graznar(self):
        print("¡Hola! Soy un humano haciendo ¡Quack!")

class Perro:
    def ladrar(self):
        print("¡Guau!")

# Esta función no pide "un objeto de tipo Pato", solo pide algo que "grazne"
def hacer_graznar(animal):
    animal.graznar()

# Creamos los objetos
pato_real = Pato()
humano = PersonaDisfrazada()
perro_fiel = Perro()

# Probamos la función
hacer_graznar(pato_real)  # Funciona: ¡Quack, quack!
hacer_graznar(humano)     # Funciona: ¡Hola! Soy un humano haciendo ¡Quack!
# hacer_graznar(perro_fiel) # ERROR: AttributeError (el perro no sabe graznar)

# Polimorfismo
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * (self.radio ** 2)

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado
    
    def calcular_area(self):
        return self.lado * self.lado

# Función polimórfica: acepta cualquier figura y calcula su área
def imprimir_area(figura):
    print(f"El área de la figura es: {figura.calcular_area():.2f}")

# Uso
circulo = Circulo(5)
cuadrado = Cuadrado(4)

imprimir_area(circulo)   # Llama al método del Círculo
imprimir_area(cuadrado)  # Llama al método del Cuadrado