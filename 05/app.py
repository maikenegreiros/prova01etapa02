from Ponto import Ponto
from Retangulo import Retangulo

print("Vamos fazer um retângulo")

x_canto1 = int(input("informe a coordenada x do canto 1: "))
y_canto1 = int(input("informe a coordenada y do canto 1: "))
x_canto2 = int(input("informe a coordenada x do canto 2: "))
y_canto2 = int(input("informe a coordenada y do canto 2: "))

ponto1 = Ponto(x_canto1, y_canto1)
ponto2 = Ponto(x_canto2, y_canto2)

retangulo = Retangulo(ponto1, ponto2)

retangulo.centro().__representacao__()