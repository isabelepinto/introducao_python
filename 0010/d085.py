total = [[], []]
for i in range(1,8):
    n = int(input(f'Digite {i}º número: '))
    if n % 2 == 0:
        total[0].append(n)
    else:
        total[1].append(n)
print(total)
print(f'Os números pares são: {sorted(total[0])}. \nOs números ímpares são {sorted(total[1])}')
