num = list()
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > num[-1]:
        num.append(n)
        print('Esse número foi adcionado ao final da lista')
    else:
        pos = 0
        while pos < len(num):
            if n <= num[pos]:
                num.insert(pos,n)
                print(f'O número foi adicionado na posição {pos}')
                break
            pos += 1
print(num)