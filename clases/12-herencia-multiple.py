class Caminador:
    def caminar(self):
        print("caminando")


class Volador:
    def volar(self):
        print("volando")


class Nadador:
    def nadar(self):
        print("nadando")


class pato(Volador, Nadador, Caminador):
    def programar(self):
        print("programando")
