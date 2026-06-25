"""
Docstring del módulo player
"""

class Player:
    """
    Clase Player
    """
    def __init__(self, name):
        self.name = name

    def play(self, song:str):
        """
        Reproduce una canción

        Args:
            song (str): Nombre de la canción
        Returns:
            int: devuelve 1 si se reproduce la canción, 0 si no
        """
        print(f"Reproduciendo {song}")
        return 1

    def stop(self):
        """
        Detiene la reproducción

        Returns:
            int: devuelve 1 si se detiene la reproducción, 0 si no
        """
        print("Deteniendo la reproducción")
        return 1
