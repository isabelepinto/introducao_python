import math
a = int(input("Digite o valor do cateto oposto: "))
b = int(input("Digite o valor do cateto adjacente: "))
#Forma 1 de fazer:
c = ((a**2)+(b**2))**0.5
#Forma 2 de fazer:
d = math.sqrt(pow(a,2) + pow(b,2))
#Forma 3 de fazer:
e = math.hypot(a,b)
print(f"O valor da hipotenusa é de {c:.2f} (maneira 1), {d:.2f} (maneira 2), {e:.2f} (maneira 3)")
