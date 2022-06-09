n = int(input("Digite um numero para saber seu fatorial: "))
f = 1
print(f"Calculando {n}! = ", end="")
for i in range(n, 0, -1):
    print(i, end=" ")
    print("x " if i > 1 else "= ", end="")
    f *= i
print(f, end=" ")