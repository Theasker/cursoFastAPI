def funcion_decoradora(funcion):
    def wrapper(*args, **kwargs):
        print("Este es el mensaje anterior...")
        funcion(*args, **kwargs)
        print("Este es el mensaje posterior;)")
    return wrapper

@funcion_decoradora
def sumar(a,b):
    print(a + b)

sumar(10,5)

