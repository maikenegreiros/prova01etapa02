class Bomba:
    def __init__(self, capacidade, preco):
        self.capacidade = capacidade
        self.preco = preco

    def abastecer_por_valor(self, valor):
        litros = valor / self.preco
        self.capacidade -= litros
        return litros

    def abastecer_por_litro(self, litros):
        custo = litros * self.preco
        self.capacidade -= litros
        return custo

    def alterar_preco(self, valor):
        self.preco = valor

    def encher_bomba(self, quantidade):
        self.capacidade += quantidade
