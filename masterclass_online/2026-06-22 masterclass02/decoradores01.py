def sumar(a, b):
    return(a+b)

def restar(a, b):
    return(a-b)

def decoradora(fn):
    num1 = int(input("Introduce un número: "))
    num2 = int(input("Introduce otro número: "))
    resultado = fn(num1, num2)
    print(resultado)

decoradora(sumar)