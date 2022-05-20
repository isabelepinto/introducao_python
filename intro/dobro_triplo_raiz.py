x = int(input("Digite um numero qualquer: "))
dobro = x * 2
triplo = x * 3
raiz = x**(1/2)
print(f"    O dobro desse numero é: {dobro}. \n    Seu triplo é: {triplo}. \n    E sua raiz é {raiz:.2f}.")
#O .2f nesse caso é apenas para configurarmos o número de casas decimais que queremos que apareca.

#Outra maneira de fazer:
x = int(input("Digite um numero qualquer: "))
print(f"    O dobro desse numero é: {x*2}. \n    Seu triplo é: {x*3}. \n    E sua raiz é {(x**(1/2)):.2f}.")