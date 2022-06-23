from random import randint
sorteio = []
jogo = []
quant = int(input('Quantos jogos você quer que eu sorteie? '))
c = 0
while c < quant:
    r = 0
    while True:
        num = randint(1,60)
        if num not in sorteio:
            sorteio.append(num)
            r += 1
        if r >= 6:
            break
    sorteio.sort()
    jogo.append(sorteio[:])
    sorteio.clear()
    c += 1
for i, l in enumerate(jogo):
    print(f'Jogo {i+1} : {l}')
      