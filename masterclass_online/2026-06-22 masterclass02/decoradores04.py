def aviso_con_argumentos(fn):
    def wrapper(*args, **kwargs):
        print('Iniciando')
        print(fn(*args, **kwargs))
        print('Finalizando')
    return wrapper

@aviso_con_argumentos
def restar(a,b):
    return a - b

@aviso_con_argumentos
def sumar(a,b):
    return a + b

restar(10,5)
