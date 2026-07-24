# Importamos el módulo datetime para trabajar con fechas y horas
import datetime

# Definición del decorador 'log' que envuelve funciones para medir su tiempo de ejecución
def log(fn):
    # Función interna (envoltura) que ejecuta la función original y mide el tiempo
    def envolt():
        # Guardamos el tiempo antes de ejecutar la función
        tiempo_inicial = datetime.datetime.now()
        
        # Ejecutamos la función decorada y mostramos su resultado
        print(fn())
        
        # Guardamos el tiempo después de ejecutar la función
        tiempo_final = datetime.datetime.now()
        
        # Mostramos la diferencia entre ambos tiempos (duración de la ejecución)
        print(f"Tiempo transcurrido: {tiempo_final - tiempo_inicial}")
    
    # Retornamos la función envoltura
    return envolt

# Aplicamos el decorador '@log' a la función get_name
# Esto significa que al llamar a get_name(), se ejecutará primero el decorador
@log
def get_name():
    # Función decorada - retorna un texto simple
    return "Texto sin procesar"

# Llamamos a la función decorada, que imprimirá el texto y el tiempo transcurrido
get_name()