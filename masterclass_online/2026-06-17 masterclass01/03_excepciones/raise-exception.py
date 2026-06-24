def division(n=0):
    if n == 0:
        raise ZeroDivisionError('No es posible dividir entre 0')
    return 10 / n

division(10)
try:
    division(0)
except ZeroDivisionError as e:
    print(e)

# podemos usar raise de forma arbitraria
try:
    raise ValueError('Error provocado por mi')
except ValueError as e:
    print(e)