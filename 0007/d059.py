n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n = int(input('''Digite a opção que você deseja:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

 '''))
while n != 5 :
    if n == 1:
        print(f"O resultado da sua soma é {n1 + n2}.")
    if n == 2:
        print(f"O resultado da multiplicação é {n1 * n2}.")
    if n == 3:
        if n1 > n2:
            print(f"O maior número escolhido é {n1}.")
        else:
            print(f"O maior número escolhido é {n2}.")
    if n == 4:
        print("Você deseja escolher dois novos números...")
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
    n = int(input('''

Digite a opção que você deseja:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

 '''))
print("Você escolheu: [5] sair do programa. Até mais!")