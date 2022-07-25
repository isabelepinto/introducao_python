import moeda

p = float(input('Digite um preço: '))
print(f'A metade de {p:.2f} é R$ {moeda.metade(p):.2f}')
print(f'O dobro de {p:.2f} é R$ {moeda.dobro(p):.2f}')
print(f'Aumentando 10% de {p:.2f} temos R$ {moeda.aumento(p):.2f}')
print(f'Reduzindo 13% de {p:.2f} temos R$ {moeda.reduzir(p):.2f}')
