from random import randint
from time import sleep

def sorteio(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        n = randint(0, 10)
        lista.append(n)
        print(n, end=' ', flush=True)
        sleep(.5)
    sleep(1)
    print('... PRONTO!')
    sleep(1)


def somar(lista):
    s = 0
    for v in lista:
        if v % 2 == 0:
            s += v
    print(f'Somando os valores pares de {lista}, temos... ', end='', flush=True)
    sleep(1)
    print(f'{s}.')
        
numeros = []
sorteio(numeros)
somar(numeros)
