class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self):
        return f"Producto: {self.nombre} - {self.precio}"

class Categoria:
    productos = []

    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos

    def agregar(self, producto):
        self.productos.append(producto)

    def imprimir(self):
        for prod in self.productos:
            print(prod)

kayak = Producto("Kayak", 275)
bicicleta = Producto("Bicicleta", 350)
patines = Producto("Patines", 45)

deportes = Categoria("Deportes", [kayak, bicicleta])
deportes.agregar(patines)

deportes.imprimir()