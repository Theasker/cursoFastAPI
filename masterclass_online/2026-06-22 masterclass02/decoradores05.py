from datetime import time
import datetime

def log(fn):
    def envolt():
        tiempo_inicial = datetime.datetime.now()
        print(fn())
        tiempo_final = datetime.datetime.now()
        print(f"Tiempo transcurrido: {tiempo_final - tiempo_inicial}")
    return envolt

@log
def get_name():
    return "Texto sin procesar"

get_name()