from random import randint
from time import sleep
from operator import itemgetter
sorteio = {'jogador1' : randint(1, 6), 'jogador2' : randint(1, 6),'jogador3' : randint(1, 6),'jogador4' : randint(1, 6)}
print('Valores sorteados: ')
for k, v in sorteio.items():
    print(f'O {k} tirou o {v}.')
    sleep(1)  
ranking = {}
ranking = sorted(sorteio.items(), key=itemgetter(1), reverse=True)
print('=*' * 30)
for x, y in enumerate(ranking):
    print(f'O {x + 1}º colocado foi o {y[0]}: com o número {y[1]}')
    sleep(1)
