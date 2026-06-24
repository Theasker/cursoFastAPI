def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError as e:
        print('Error: No se puede dividir por cero.')
    else:
        print(resultado)
    finally:
        print("Se acabó la división.")

dividir(10, 0)