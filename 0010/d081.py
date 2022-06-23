lista = list()
while True:
    lista.append(int(input("Digite um valor: ")))
    continuar = str(input('Deseja continuar?[S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
    while continuar not in 'NS':
        continuar = str(input('Não entendi. Deseja continuar?[S/N] ')).upper().strip()[0]
print(f'Foram digitados {len(lista)} valores.')
lista.sort(reverse=True)
print(f'A lista ordenada decrescente é {lista}.')
if 5 in lista:
    print('O número 5 está dentro de lista!')
else:
    print('Infelizmente não encontramos o número 5...')