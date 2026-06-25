def aviso(fn):
    def envoltura(titulo):
        print("Iniciando tarea ...")
        print(fn(titulo))
        print("Terminando tarea...")
    return envoltura

@aviso
def tarea(titulo):
    return f"La tarea {titulo} debe ser completada."

@aviso
def cenar(plato):
    return f"La cena es {plato}."

tarea('Estudiar python')
cenar('Pasta')