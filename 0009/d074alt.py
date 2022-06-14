from random import randint
numeros = (randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9))
print('Os números sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior número é o {max(numeros)}. \nO menor número é o {min(numeros)}.')