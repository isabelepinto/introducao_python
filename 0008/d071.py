print('=' * 30)
print('{: ^30}'.format('BANCO ISABELE'))
print('=' * 30)
sacar = int(input("Qual valor será sacado? "))
#cédulas de R$50, R$20, R$10, R$1
cinquenta = sacar//50
r50 = sacar % 50
vinte = r50//20
r20 = r50 % 20
dez = r20//10
r10 = r20 % 10
cinco = r10//5
r5 = r10 % 5
um = r5
print(f'''Total de {cinquenta} cédulas de R$50,00
Total de {vinte} cédulas de R$20,00
Total de {dez} cédulas de R$10,00
Total de {cinco} cédulas de R$5,00
Total de {um} cédulas de R$1,00

Volte sempre ao nosso Banco!''')