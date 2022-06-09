n = int(input("Digite um numero para saber seu fatorial: "))
c = n
f = 1 #fato nulo de multificação é 1 e de soma é 0
print(f"Calculando {n}! = ", end=" ")
while c > 0:
    print(c, end=" ")
    print("x" if c > 1 else "=", end=" ")
    f *= c
    c -= 1
print(f)