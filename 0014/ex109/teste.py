import moeda

p = float(input('Digite um preço: '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, False)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p)}')
print(f'Aumentando 10% de {moeda.moeda(p)} temos {moeda.aumento(p, 10)}')
print(f'Reduzindo 13% de {moeda.moeda(p)} temos {moeda.reduzir(p, 13)}')
