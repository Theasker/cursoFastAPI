class Model():
    tabla = False

    def __init__(self):
        if not self.tabla:
            print("Error: Debes definir una tabla para la clase")
    
    def guardar(self):
        print(f"Guardando {self.tabla} en BBDD")
    
    @classmethod
    def buscar_por_id(self, _id):
        print(f"Buscando por id {_id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = "usuario"

usuario = Usuario()
usuario.guardar()
Usuario.buscar_por_id(5)