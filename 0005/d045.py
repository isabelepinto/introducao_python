from random import randint
from time import sleep
print("Vamos jogar Jokenpô comigo?")
opcoes = ("pedra", "papel", "tesoura")
escolha = str(input('''Escolha uma das opções: 
pedra 
papel
tesoura
'''))
print(" \n \n")
pc = opcoes[randint(0,2)]
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ!")
print("-="*20)
sleep(1)
print(f"Eu escolhi {pc} ...\nVocê escolheu {escolha}...")
print("-="*20)
if pc == escolha:
    print("Nós empatamos.")
elif pc == "tesoura" and escolha == "pedra" or pc == "pedra" and escolha == "papel" or pc == "papel" and escolha == "tesoura":
    print("Parabéns! Você venceu!")
else:
    print("Eu venci. Ninguém é melhor que eu nesse jogo! hahahaha.")