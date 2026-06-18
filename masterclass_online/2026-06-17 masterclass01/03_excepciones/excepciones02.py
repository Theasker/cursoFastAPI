class MiError(Exception):
    pass

class ConexionError(Exception):
    pass


try:
    numero = int(input("Ingrese un número: "))
    if numero < 0:
        raise MiError('El número no puede ser negativo')
    print(numero)
except MiError as e:
    print(f'Error MiError: {e}')
except Exception:
    print('Error desconocido')






