num = list()
while True:
    a = int(input('Digite um valor: '))
    if a in num:
        print('Valor duplicado! Não vou adicionar...')
    if a not in num:
        num.append(a)
        print('Valor adcionado com sucesso!')
    continuar = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    while continuar not in 'NS':
        continuar = str(input('Não entendi... Deseja continuar? [S/N]')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'Você digitou os valores: {sorted(num)}')