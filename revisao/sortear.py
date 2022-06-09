from random import randint
from time import sleep
nome = str(input('Olá. Qual o seu nome ? ')).strip ()
print ('Tudo bem, {}? \n \nVou escolher um exercício para você revisar...'.format (nome))
exercicio = randint (1,100)
print('Escolhendo...')
sleep(1)
print('3')
sleep(1)
print('2')
sleep (1)
print('1')
sleep(1)
print ('Achei um bem legal! \nVocê vai revisar o exercício {} '.format (exercicio))