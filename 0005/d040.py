n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
media = (n1 + n2) / 2
if media < 5.0:
    print("REPROVADO")
elif 7 > media >= 5.0:
    print("RECUPERAÇÃO")
else:
    print("APROVADO")