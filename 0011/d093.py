futebol = dict()
aproveitamento = list()
s = 0
futebol['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas o {futebol["nome"]} jogou? '))
for c in range(0, partidas):
    gol = int(input(f'  Quantos gols na partida {c}? '))
    aproveitamento.append(gol)
    s += gol
futebol['gols'] = aproveitamento[:]
futebol['total'] = s
print('=-'*30)
print()
print(futebol)
print()
print('=-'*30)
for k, v in futebol.items():
    print(f'{k} tem valor {v}.')
print()
print('=-'*30)
print(f'O jogador {futebol["nome"]} jogou {partidas} partidas.')
for v, x in enumerate(aproveitamento):
    print(f'    => Na partida {v}, fez {x} gols.')
print(f'Foi um total de {partidas} partidas.')