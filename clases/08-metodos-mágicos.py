class Perro:
    def __init__(self, nombre, edad):
        self.nombre = (nombre)
        self.edad = edad

    def __del__(self):
        print(f"Chao Perro 😔 {self.nombre}")

    def __str__(self):
        return f"Clase Perro: {self.nombre}"

    def habla(self):
        print(f"{self.nombre} dice: Guau!")


perro = Perro("Chanchito", 7)
del perro
