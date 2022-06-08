distancia = float(input("Qual a distancia da sua viagem? "))
valor1 = distancia * 0.50
valor2 = distancia * 0.45
if distancia <= 200:
    print(f"O valor da sua viagem será de {valor1:.2f} reais.")
else:
    print(f"O valor da sua viagem será de {valor2:.2f} reais.")