from snack import Snack
from servicio_snacks import ServicioSnacks

class MaquinaSnacks:
    def __init__(self):
        self.servicio_snacks = ServicioSnacks()
        # Productos de la compra actual
        self.productos = []

    def maquina_snacks(self):
        salir = False
        print('*** Máquina de Sancks ***')
        self.servicio_snacks.mostrar_snacks()
        while not salir:
            try:
                opcion = self.mostrar_menu()
                salir = self.ejecutar_opcion(opcion)
            except Exception as e:
                print(f'Error: {e}')

    def mostrar_menu(self):
        print(f'''Menu:
        1. Comprar snack
        2. Mostrar ticket
        3. Agregar Nuevo Snack al inventario
        4. Mostrar inventario de Snacks
        5. Salir''')
        return int(input('Elige una opción: '))

    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            self.comprar_snack()
        elif opcion == 2:
            self.mostrar_ticket()
        elif opcion == 3:
            self.agregar_snack()
        elif opcion == 4:
            self.servicio_snacks.mostrar_snacks()
        elif opcion == 5:
            print('Vuelve pronto!')
            return True
        else:
            print(f'Opción no válida: {opcion}')
        return False

    def comprar_snack(self):
        id_snack = int(input('¿Qué snack deseas comprar (id)? '))
        snack = next((snack for snack in self.servicio_snacks.get_snacks() if snack.id_snack == id_snack), None)
        if snack:
            self.productos.append(snack)
            print(f"Snack encontrado: {snack}")
        else:
            print('Snack no encontrado')

    def mostrar_ticket(self):
        # Muestra todos los productos guardados
        if not self.productos:
            print('No hay productos en el ticket')
            return
        total = sum(snack.precio for snack in self.productos)
        print('--- Ticket de Venta ---')
        for producto in self.productos:
            print(f'\t- {producto.nombre} - {producto.precio:.2f}')
        print(f'Total: {total:.2f}')
        print('----------------')

    def agregar_snack(self):
        nombre = input('Nombre del snack: ')
        precio = float(input('Precio del snack: '))
        nuevo_snack = Snack(nombre, precio)
        self.servicio_snacks.agregar_snack(nuevo_snack)
        print('Snack agregado al inventario')

if __name__ == '__main__':
    maquina_snacks = MaquinaSnacks()
    maquina_snacks.maquina_snacks()