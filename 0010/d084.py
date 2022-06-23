pessoas = []
todes = []
maior = menor = 0
while True:
    pessoas.append(str(input('Qual seu nome? ')).capitalize())
    pessoas.append(float(input('Qual seu peso? ')))
    if len(todes) == 0:
        menor = maior = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]
    todes.append(pessoas[:])
    pessoas.clear()
    continuar = str(input('Deseja continuar?[S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
    while continuar not in 'NS':
        continuar = str(input('Não entendi. Deseja continuar?[S/N]: ')).upper().strip()[0]
print(f'Você cadastrou {len(todes)} pessoas.')
print(f'O maior peso é de {maior} Kg. Peso de ',end='')
for p in todes:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print(f'\nO menor peso é de {menor} Kg. Peso de ',end='')
for p in todes:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
