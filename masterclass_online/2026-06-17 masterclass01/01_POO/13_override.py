class Ave:
    def __init__(self):
        self.volador = "volador"

    def vuela(self):
        print("Volando ave...")

class Pato(Ave):
    def __init__(self):
        super().__init__()
        self.nadador = "nadador"

    def vuela(self):
        super().vuela()
        print("Volando pato...")

pato = Pato()
pato.vuela()
print(pato.volador, pato.nadador)
