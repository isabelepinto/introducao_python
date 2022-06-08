maior = 0
menor = 0
for n in range(1, 6):
    peso = float(input(f"Qual o peso da {n}ª pessoa? "))
    if n == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f"O maior peso é {maior}kg e o menor peso é {menor}kg.")
    