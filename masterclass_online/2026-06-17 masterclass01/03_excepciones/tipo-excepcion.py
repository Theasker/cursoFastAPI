# De esta manera podemos saber que tipo de error nos dio el programa
try:
    n1 = int(input('Digite un numero: '))
except Exception as e:
    print(type(e))

# De esta manera podemos ver el error en especifico
try:
    n1 = int(input('Digite un numero: '))
except ValueError as e:
    print(e)