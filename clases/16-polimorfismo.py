class Usuario():
    def guardar(self):
        print("Guardando en BBDD")


class Sesion():
    def guardar(self):
        print("Guardando en Archivo")


def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()


usuario = Usuario()
sesion = Sesion()

guardar([sesion, usuario])
