"""
Esta es el modulo que incluye 
la clase del reproductor de música
"""

class Player:
    """
    Esta clase crea un reproductor
    de música
    """

    def play(self, song):
        """
        Reproduce la canción que recibió como parámetro
        
        Parameters:
        song(str): este es un string con el path de la canción
        
        Returns:
        int: devuelve 1 si reproduce con éxito, en el caso de fracaso devuelve 0
        """
        print("reproduciendo canción")

    def stop(self):
        print("stopping")