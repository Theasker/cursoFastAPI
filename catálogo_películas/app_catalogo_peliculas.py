from servicio_peliculas import ServicioPeliculas
from pelicula import Pelicula

class AppCatalogoPeliculas:

    def __init__(self):
        self.servicio_peliculas = ServicioPeliculas()

    def mostrar_menu(self):
        print('*** App Catálogo de películas ***')
        while True:
            try:
                print(f'''Opciones:
                    1. Agregar película
                    2. Listar películas
                    3. Eliminar catálogo de películas
                    4. Salir
                      ''')
                opcion = int(input('Selecciona una opción (1-4): '))
                if opcion == 1:
                    nombre_pelicula = input('Introduce el nombre de la película: ')
                    pelicula = Pelicula(nombre_pelicula)
                    self.servicio_peliculas.agregar_pelicula(pelicula)
                elif opcion == 2:
                    self.servicio_peliculas.listar_peliculas()
                elif opcion == 3:
                    self.servicio_peliculas.eliminar_archivo_peliculas()
                elif opcion == 4:
                    print('Saliendo de la aplicación...')
                    break
                else:
                    print('Opción incorrecta\nSelecciona una opción (1-4):')
                    
            except ValueError:
                print('Error: Introduce un número válido.')
            except Exception as e:
                print(f'Error: {e}')

if __name__ == '__main__':
    app = AppCatalogoPeliculas()
    app.mostrar_menu()