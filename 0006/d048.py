s = 0
cont = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        cont = cont + 1
        s = n + s
print(f"A soma de todos o {cont} valores solicitados é {s}.")