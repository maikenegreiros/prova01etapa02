class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1 
        self.crescer()
    
    def engordar(self, kg):
        self.peso += kg
    
    def emagrecer(self, kg):
        self.peso -= kg
    
    def crescer(self):
        if (self.idade >= 21): return
        self.altura += 0.05
