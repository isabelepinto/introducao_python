n = int(input("Digite um número inteiro: "))
count = 0
for c in range(1, n+1):
    if n % c == 0:
        count += 1
print(f"Esse numero foi divisivel {count} vezes.")
if count > 2:
    print("Por isso, NÃO é um número primo.")
else:
    print("Então, ele é um número primo.")