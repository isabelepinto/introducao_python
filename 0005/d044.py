preco = float(input("Digite o preço do produto: "))
print('''Formas de Pagamento:
1 - à vista dinheiro/cheque;
2 - à vista cartão;
3 - 2x no cartão;
4 - 3x ou mais no cartão;''')
opcao = int(input("Qual é a opção de pagamento? \n"))
if opcao == 1:
    total = preco * 0.9
elif opcao == 2:
    total = preco * 0.95
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f"Sua compra será parcelada em 2x de R${parcela:.2f}, sem juros.")
elif opcao == 4:
    total = preco * 1.2
    totparc = int(input("Em quantas parcelas? "))
    parcela = total/totparc
    print(f"Sua compra será parcelada em {totparc} de R$ {parcela:.2f}, com juros.")
else:
    total = preco
    print("A opção que você digitou não existe em nosso sitema. Tente novamente!") 
print(f"Sua compra de R${preco:.2f} vai custar R${total:.2f} no final.")
