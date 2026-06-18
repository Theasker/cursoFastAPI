import codecs
class Coordenadas:
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng
    
    # comparación de igualdad
    def __eq__(self, otro):
        return self.lat == otro.lat and self.lng == otro.lng
    
    # comparación de desigualdad
    def __ne__(self, other):
        return self.lat != other.lat or self.lng != other.lng
    
    # Comparación menor que
    def __lt__(self, other):
        return self.lat < other.lat or self.lng < other.lng
    
    # comparación menor o igual que
    def __le__(self, other):
        return self.lat <= other.lat or self.lng <= other.lng
    
    # comparación mayor que
    def __gt__(self, other):
        return self.lat > other.lat or self.lng > other.lng
    
    # comparación mayor o igual que
    def __ge__(self, other):
        return self.lat >= other.lat or self.lng >= other.lng

coords = Coordenadas(10, 20)
coords2 = Coordenadas(10, 20)

print(coords == coords2)
print(coords < coords2)
print(coords > coords2)
print(coords <= coords2)
print(coords >= coords2)
print(coords != coords2)
