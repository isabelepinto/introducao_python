from random import randint
a = randint(0, 9)
b = randint(0, 9)
c = randint(0, 9)
d = randint(0, 9)
e = randint(0, 9)
sorteio = (a, b, c, d, e)
print('Os números sorteados foram: ', end="")
for s in sorteio:
    print(s, end=" ")
ordem = sorted(sorteio)
print(f'\nO maior número sorteado foi o {ordem[4]}')
print(f'O menor número sorteado foi o {ordem[0]}')
