num = list()
for n in range(0,5):
    num.append(int(input(f'Digite o valor para a posição {n}: ')))
print(f'A lista formada foi: {num}')
print(f'O maior valor digitado foi o {max(num)} na posição ',end='')
for c, v in enumerate(num):
    if v >= max(num):
        print(f'{c}...',end='')
print(f'\nO menor valor digitado foi o {min(num)} na posição ',end='')
for c, v in enumerate(num):
    if v <= min(num):
        print(f'{c}...',end='')
print('\nFIM')