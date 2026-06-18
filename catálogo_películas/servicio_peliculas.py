import os

class ServicioPeliculas:
    def __init__(self):
        self.nombre_archivo = 'peliculas.txt'
    
    def agregar_pelicula(self, pelicula):
        with open(self.nombre_archivo, 'a', encoding="utf-8") as archivo:
            archivo.write(pelicula.nombre + '\n')
    
    def listar_peliculas(self):
        peliculas = []
        if os.path.exists(self.nombre_archivo):
            with open(self.nombre_archivo, 'r', encoding="utf-8") as archivo:
                print('--- Listado de peliculas ---')
                print(archivo.read())
        else:
            print('El archivo no existe')
    
    def eliminar_archivo_peliculas(self):
        try:
            os.remove(self.nombre_archivo)
            print('Archivo eliminado correctamente')
        except FileNotFoundError:
            print('El archivo no existe')
            