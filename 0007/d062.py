a1 = int(input("Digite o a1: "))
r = int(input("Digite a razão: "))
n = 0
n2 = 0
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while n < total:
        a = a1 + (r*n)
        n += 1
        print(a, end=" ")
        print("-> ", end=" ")
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print(f"ACABOU. Foram usados {n} termos nessa P.A.")