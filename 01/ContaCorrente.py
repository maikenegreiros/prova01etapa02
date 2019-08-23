class ContaCorrente:
    def __init__(self, numero, correntista, saldo = 0):
        self.numero = numero
        self.correntista = correntista
        self.saldo = saldo

    def alterar_nome(self, nome):
        self.correntista = nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if (valor > self.saldo):
            print("Saldo insuficiente")
            return
        self.saldo -= valor
