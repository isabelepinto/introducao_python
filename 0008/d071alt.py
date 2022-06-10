sacar = int(input("Quantos reais você deseja sacar? R$ "))
total = sacar
nota = 50
quantas = 0
while True:
    if total >= nota:
        total = total - nota
        quantas += 1
    else:
        if quantas > 0:
            print(f"Total de {quantas} notas de R${nota:.2f}.")
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 5
        elif nota == 5:
            nota = 1
        quantas = 0
        if total == 0:
            break