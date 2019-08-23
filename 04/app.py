from Bomba import Bomba

bomba = Bomba(1000, 4)

def printAttributes():
    print("capacidade:", bomba.capacidade)
    print("preco:", bomba.preco)

printAttributes()
litros_gastos = bomba.abastecer_por_valor(8)
print("litros_gastos:", litros_gastos)
custo = bomba.abastecer_por_litro(4)
print("custo:", custo)
bomba.alterar_preco(2)
bomba.encher_bomba(1000)
printAttributes()