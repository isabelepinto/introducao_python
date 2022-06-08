s = 0
cont = 0
for i in range(0, 6):
    n = int(input("Digite o número: "))
    if n % 2 == 0:
        s += n
        cont += 1
print(f"A soma dos {cont} números pares é {s}.")
