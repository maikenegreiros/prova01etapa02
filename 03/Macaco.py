class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, comida):
        self.bucho.append(comida)

    def ver_bucho(self):
        print(self.bucho or self.nome + " está de estômago vazio")

    def digerir(self):
        self.bucho = []
