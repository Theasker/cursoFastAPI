class Usuario():
    def guardar(self):
        print("Guardando usuario en BBDD")

class Sesion():
    def guardar(self):
        print("Guardando en archivo")

def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()

usuario = Usuario()
sesion = Sesion()
guardar([sesion, usuario])
