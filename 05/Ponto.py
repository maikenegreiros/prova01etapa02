class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __representacao__(self):
        print(self.x, self.y, sep=",")
        