def deco(fn):
    def wrapper():
        print("Inicio")
        fn()
        print("Fin")
    return wrapper

@deco
def saludar():
    print("Hola")


saludar()