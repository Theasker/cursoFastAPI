def prueba(*argumentos):
    print(f'argumentos: {argumentos} // de tipo: {type(argumentos)}')

prueba('hola', 'que', 'tal', 'estas')
print('------------------------------')
def registrar_usuario(**clavevalor):
    # kwargs es un DICCIONARIO: {'nombre': 'Alex', 'edad': 28, 'rol': 'Admin'}
    print(f'kwargs: {clavevalor} // de tipo: {type(clavevalor)}')
    if clavevalor['rol']:
        print(f"clavevalor['rol']: {clavevalor["rol"]}")

registrar_usuario(nombre="Alex", edad=28, rol="Admin")