from ..gestion.crud import guardar

def pagar_impuestos():
    print("Pagando impuestos...")
    guardar()

if __name__ == "__main__":
    pagar_impuestos()