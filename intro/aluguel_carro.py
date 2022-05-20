dias = int(input("Insira o numero de dias alugado: "))
km = float(input("Insira os km percorridos: "))
preco_total = (dias * 60) + (km * 0.15)
print(f"O valor do aluguel do carro foi o total de {preco_total:.2f} reais.")