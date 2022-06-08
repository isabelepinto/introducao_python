a1 = int(input("Digite o primeiro terma da P.A.: "))
r = int(input("Digite a razão da P.A.: "))
for n in range(1, 11):
    an = a1 + (n-1)*r
    print(an, end="-> ")
print("ACABOU")
