n = int(input("Digite um numero: "))
a1 = 0
a2 = 1
a = 0
x = 0
if n == 1:
    print(f"A sequência de Fibonacci com {n} elementos é: {a1}")
elif n == 2:
    print(f"A sequência de Fibonacci com {n} elementos é: {a1} {a2}")
else:
    print(f"A sequência de Fibonacci com {n} elementos é: {a1} {a2}", end=" ")
    while x < (n - 2):
        an = (a1) + (a2)
        a1 = a2
        a2 = an
        x += 1
        print(an, end=" ")
