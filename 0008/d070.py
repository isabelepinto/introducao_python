s = c = count = barato = 0
maisbarato = " "
while True:
    nome = str(input("Qual o nome do produto? ")).upper().strip()
    preco = float(input("Qual o preço do produto? R$ "))
    s += preco
    count += 1
    if preco > 1000:
        c += 1
    if count == 1 or preco < barato:
        barato = preco
        maisbarato = nome
    continuar = " "
    while continuar not in "SsNs":
        continuar = str(input("Deseja continuar?[S/N]")).upper().strip()[0]
    if continuar in "Nn":
        break
print(f"O total gasto na compra foi de R${s:.2f}.\nSendo que {c} custaram mais de R$1.000 e o produto mais barato foi {maisbarato}.")
print("\nFIM DO PROGRAMA")