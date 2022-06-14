valores = (int(input("Digite um valor: ")), 
           int(input("Digite um valor: ")), 
           int(input("Digite um valor: ")), 
           int(input("Digite um valor: ")))
print(f'Você digitou os valores: {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes.')
if valores.count(3) > 0:
    print(f'O valor 3 foi digitado a primeira vez na {valores.index(3) + 1}ª posição.')
else:
    print('O valor 3 não foi encontrado.')
pares = 0
for v in valores:
    if v % 2 == 0:
        pares += 1
if pares == 0:
    print('Não há valor par nessa sequência.')
elif pares > 0:
    print('Os valores pares encontrados foram: ', end='')
    for v in valores:
        if v % 2 == 0:
            print(v, end=' ')
