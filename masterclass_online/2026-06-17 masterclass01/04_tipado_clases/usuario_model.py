class Estudiante():
    # atributos de clase
    nombre: str
    edad: int
    email: str
    password: str
    estado: bool

    def __init__(self, nombre: str, edad: int, email: str, password: str):
        # atributos de instancia
        self.nombre = nombre
        self.edad = edad
        self.email = email
        self.password = password
        self.estado = True

    # setter
    def actualizar_nombre(self, nombre: str):
        self.nombre = nombre

    # getter
    def mostrar_nombre(self):
        print(self.nombre)

alumno = Estudiante('Ana', 20, 'and@gmail.com', '123456')
print(alumno.mostrar_nombre())