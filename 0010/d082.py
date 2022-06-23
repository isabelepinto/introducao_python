lista = list()
while True:
    lista.append(int(input("Digite um valor: ")))
    continuar = str(input('Deseja continuar?[S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
    while continuar not in 'NS':
        continuar = str(input('Não entendi. Deseja continuar?[S/N] ')).upper().strip()[0]
print(f'A lista original é {lista}.')
par = list()
impar = list()
for c, l in enumerate(lista):
    if l % 2 == 0:
        par.append(l)
    else:
        impar.append(l)
print(f'A lista com números pares é {par}.')
print(f'A lista com números ímpares é {impar}.')
