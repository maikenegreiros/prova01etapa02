from ContaCorrente import ContaCorrente

conta = ContaCorrente(123, 'Maike', 150.58)

print(conta.numero)
print(conta.correntista)
print(conta.saldo)
conta.deposito(200)
print(conta.saldo)
conta.saque(300)
print(conta.saldo)
conta.saque(300)
conta.alterar_nome('AJ')
print(conta.saldo)
print(conta.correntista)