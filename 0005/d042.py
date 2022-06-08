l1 = float(input("Digite o lado 1: "))
l2 = float(input("Digite o lado 2: "))
l3 = float(input("Digite o lado 3: "))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    if l1 == l2 == l3:
        print("Esse é um triângulo equilátero.")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("Esse é um triângulo isósceles.")
    else:
        print("Esse é um triângulo escaleno.")
else:
    print("Esses segmentos não formam um triângulo.")