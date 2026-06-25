def aviso(fn, titulo, prioridad):
    def envoltura():
        print("Aviso, va a empezar la función")
        print(fn(titulo, prioridad))
        print("Fin de la función")
    return envoltura

def tarea(titulo, prioridad):
    if prioridad == 1:
        return f"La tarea {titulo} es de alta prioridad."
    elif prioridad == 2:
        return f"La tarea {titulo} es de baja prioridad."
    else:
        return "PRIORIDAD DESCONOCIDA"


# print(tarea('Estudiar', 1))

tarea_con_aviso = aviso(tarea, 'estudiar', 1)
print(tarea_con_aviso())