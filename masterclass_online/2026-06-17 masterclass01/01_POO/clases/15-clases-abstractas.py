from abc import ABC, abstractmethod

class Model(ABC):
    @property
    @abstractmethod
    def tabla(self):
        pass

    @abstractmethod
    def guardar(self):
        pass
    
    @classmethod
    def buscar_por_id(self, _id):
        print(f"Buscando por id {_id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = "usuario"

    def guardar(self):
        print(f"Guardando usuario en la tabla {self.tabla} en BBDD")


usuario = Usuario()
usuario.guardar()
Usuario.buscar_por_id(5)

