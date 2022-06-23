matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = somaterceira = 0
#obtendo o input da matriz
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite o valor [{l}, {c}]: '))
#imprimindo o output formatado
for l in range(0,3):
    for c in range(0,3):
        print(f'[  {matriz[l][c]}  ]', end=' ')
        #realizando a soma dos números pares
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print(f'A soma dos números pares da matriz é {spar}.')
#realizando a soma dos elementos da terceira coluna
for l in range(0,3):
    somaterceira += matriz[l][2]
print(f'A soma dos números da terceira coluna é {somaterceira}.')
#pegando o maior valor da segunda linha
print(f'O maior valor da segunda linha é {max(matriz[1])}.')