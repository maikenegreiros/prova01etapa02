from Ponto import Ponto

class Retangulo:
    def __init__(self, canto1, canto2):
        self.canto1 = canto1
        self.canto2 = canto2

    def centro(self):
        x = (self.canto2.x - self.canto1.x) / 2
        y = (self.canto2.y - self.canto1.y) / 2
        return Ponto(x, y)
