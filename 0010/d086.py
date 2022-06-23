linha1 = []
linha2 = []
linha3 = []
matriz = []
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
