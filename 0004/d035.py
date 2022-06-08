n1 = float(input("Digite o segmento 1: "))
n2 = float(input("Digite o segmento 2: "))
n3 = float(input("Digite o segmento 3: "))
if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print(f"O perímetro do triângulo é de: {n1 + n2 + n3}")
else:
    print("Esses segmentos de reta não formam um triângulo")
