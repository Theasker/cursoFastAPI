class MiError(Exception):
    "Esta clase representa errores personalizados"

    def __init__(self, message, error_code):
        self.message = message
        self.error_code = error_code

    def __str__(self):
        return f'Error: {self.error_code} - {self.message}'

def division(n=0):
    if n == 0:
        raise MiError('No se puede dividir entre 0', 805)
    return 10 / n

try:
    division()
except MiError as e:
    print(e)