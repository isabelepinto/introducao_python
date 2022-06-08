from math import trunc
real = float(input("Digite um numero real: "))
inteiro = trunc(real)
print(f"O número {real} tem a parte inteira {inteiro}")

#Outra forma de fazer (sem precisar importar bibliotecas):
real2 = float(input("Digite um numero real: "))
print(f"O número {real2} tem a parte inteira {int(real2)}")