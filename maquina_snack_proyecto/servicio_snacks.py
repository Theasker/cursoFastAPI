import os.path
from snack import Snack

class ServicioSnacks:
    NOMBRE_ARCHIVO = 'snacks.txt'

    def __init__(self):
        self.snacks = []
        # Revisar si ya existe el sarchivo snacks
        # Si ya existe, obtenemos los snacks del archiv
        if os.path.isfile(self.NOMBRE_ARCHIVO):
            self.snacks = self.obtener_snacks()
        # Sino, cargamos algunos snacks iniciales
        else:
            self.cargar_snacks_iniciales()

    def cargar_snacks_iniciales(self):
        snacks_iniciales = [
            Snack('Papas', 70),
            Snack('Refresco', 50),
            Snack('Sandwich', 100)
        ]
        self.snacks.extend(snacks_iniciales)
        self.guardar_snacks_archivo(snacks_iniciales)

    def guardar_snacks_archivo(self, snacks):
        try:
            with open(self.NOMBRE_ARCHIVO, 'a') as archivo:
                for snack in snacks:
                    archivo.write(snack.escribir_snack() + '\n')
        except Exception as e:
            print(f'Error al guardar los snacks: {e}')

    def obtener_snacks(self):
        snacks = []
        try:
            with open(self.NOMBRE_ARCHIVO, 'r') as archivo:
                for linea in archivo:
                    id_snack, nombre, precio = [item.strip() for item in linea.split(',')]
                    snack = Snack(nombre, float(precio))
                    snack.id_snack = int(id_snack)
                    Snack.contador_snacks = max(Snack.contador_snacks, snack.id_snack)
                    snacks.append(snack)
            
        except Exception as e:
            print(f'Error al leer archivo de snacks: {e}')
        return snacks

    def agregar_snack(self, snack):
        self.snacks.append(snack)
        self.guardar_snacks_archivo([snack])

    def mostrar_snacks(self):
        print('--- Snacks en inventario ---')
        for snack in self.snacks:
            print(snack)
        print('----------------------------')

    def get_snacks(self):
        return self.snacks


if __name__ == '__main__':
    servicio_snacks = ServicioSnacks()
    print(servicio_snacks.snacks)
