times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 
'Atlético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos', 'Bahia', 
'Corinthians', 'Fluminense', 'Ceará', 'Vasco da Gama', 'Sport Recife', 
'América-MG', 'Chapecoense', 'Vitória', 'Paraná')
print(" ")
print('-=' * 25)
print('\nOs cinco primeiros colocados são:')
for t in range(0,5):
    print(f'O {t + 1}º colocado é: {times[t]}')
print(" ")
print('-=' * 25)
print('\nOs últimos quatro colocados são: ')
for t in range(len(times) - 4, len(times)):
    print(f'{t + 1}º: {times[t]}')
print(" ")
print('-=' * 25)
print(f'\nOs times em ordem alfabética são: ')
ordem = sorted(times)
for o in ordem:
    print(o)
posicao = times.index('Chapecoense')
print(" ")
print('-=' * 25)
print(f'\nO time Chapecoense está na {posicao + 1}ª posição.')
print(" ")
print('-=' * 25)
