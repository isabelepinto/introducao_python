from random import randint
from time import sleep
c = 0
d = 0
while True:
    pc = randint(0,10)
    opcao = str(input('Ímpar ou par: ')).strip().upper()[0]
    jogador = int(input('Digite seu número: '))
    while opcao not in "PpIi":
        opcao = str(input('Ímpar ou par: ')).strip().upper()[0]
    soma = pc + jogador
    sleep(1)
    print('1, 2, 3, meia e.... ')
    sleep(1)
    print('JÁ')
    sleep(1)
    if opcao in 'ÍI': 
        if soma % 2 == 0:
            print(f'Você escolheu {opcao}. \nEu coloquei o número {pc} e você o número {jogador}. \nEu venci! Ninguém é melhor que eu nesse jogo!')
            break
        else:
            print(f'Você escolheu {opcao}. \nEu coloquei o número {pc} e você o número {jogador}. \nVocê venceu! Parabéns!')
            c += 1
    elif opcao in 'P': 
        if soma % 2 != 0:
            print(f'Você escolheu {opcao}. \nEu coloquei o número {pc} e você o número {jogador}. \nEu venci! Ninguém é melhor que eu nesse jogo!')
            break
        else:
            print(f'Você escolheu {opcao}. \nEu coloquei o número {pc} e você o número {jogador}. \nVocê venceu! Parabéns!')
            d += 1
print(f"Você acertou {c + d} vezes consecutivas!")
    