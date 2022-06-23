linha1 = []
linha2 = []
linha3 = []
matriz = []
s1 = s2 = s3 = 0
for i in range(0,3):
    n = int(input(f'Digite um número na posição [0,{i}]: '))
    linha1.append(n)
for i in range(0,3):
    n = int(input(f'Digite um número na posição [1,{i}]: '))
    linha2.append(n)
for i in range(0,3):
    n = int(input(f'Digite um número na posição [2,{i}]: '))
    linha3.append(n)
matriz.append(linha1[:])
matriz.append(linha2[:])
matriz.append(linha3[:])
print(f'[ {matriz[0][0]} ] [ {matriz[0][1]} ] [ {matriz[0][2]} ]')
print(f'[ {matriz[1][0]} ] [ {matriz[1][1]} ] [ {matriz[1][2]} ]')
print(f'[ {matriz[2][0]} ] [ {matriz[2][1]} ] [ {matriz[2][2]} ]')
for v in linha1:
    if v % 2 == 0:
        s1 += v
for v in linha2:
    if v % 2 == 0:
        s2 += v 
for v in linha3:
    if v % 2 == 0:
        s3 += v  
print(f'A soma dos valores pares é {s1 + s2 + s3}.') 
print(f'A soma dos valores da 3ª coluna é {(matriz[0][2]) + (matriz[1][2]) + (matriz[2][2])}.')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
