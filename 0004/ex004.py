tempo = int(input("Quantos anos tem seu carro? "))
if tempo <= 3:
    print("Seu carro esta novo!")
else:
    print("Seu carro precisa ser trocado!")
print("--FIM--")

# Forma simplificada:
print("Seu carro está novo!" if tempo <= 3 else "Seu carro está velho!")
print("--FIM--")