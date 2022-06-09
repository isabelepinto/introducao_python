n = c = s = maior = menor = 0
continuar = ""
while continuar in "YESyes":
    n = int(input("Digite um número inteiro: "))
    c += 1
    s += n
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    continuar = str(input("Deseja continuar? [yes/no]: ")).strip().upper()[0]
media = s/c
print(f"A média entre os {c} valores escolhidos é: {media}. \nSendo o maior valor {maior} e o menor valor {menor}.")   