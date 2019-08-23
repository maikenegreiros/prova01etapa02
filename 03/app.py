from Macaco import Macaco

def alimentarMacaco(macaco):
    refeicoes = 0 
    while(refeicoes < 3):
        refeicao = input("Digite um alimento para para o {} comer: ".format(macaco.nome))
        macaco.comer(refeicao)
        refeicoes += 1
        print("bucho do macaco", macaco.nome, ":", end=" ")
        macaco.ver_bucho()

nome1 = input("Dê um nome para o primeiro macaco: ")
macaco1 = Macaco(nome1)
alimentarMacaco(macaco1)

nome2 = input("\nAgora dê um nome para o segundo macaco: ")
macaco2 = Macaco(nome2)
alimentarMacaco(macaco2)

