a1 = int(input("Digite o a1: "))
r = int(input("Digite a razão: "))
n = 0
while n < 10:
    a = a1 + (r*n)
    n += 1
    print(a, end=" ")
    print("-> ", end=" ")
print("FIM")
