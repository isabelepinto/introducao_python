import moeda

p = float(input('Digite um preço: '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'Aumentando 10% de {moeda.moeda(p)} temos {moeda.moeda(moeda.aumento(p,10))}')
