from Pessoa import Pessoa

pessoa = Pessoa('Maike', 18, 60, 1.65)

def printAttributes():
    print(pessoa.nome)
    print(pessoa.idade)
    print(pessoa.peso)
    print(pessoa.altura)

printAttributes()
pessoa.envelhecer()
printAttributes()