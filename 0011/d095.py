futebol = dict()
aproveitamento = list()
todos = []
s = 0
while True:
    futebol['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas o {futebol["nome"]} jogou? '))
    for c in range(0, partidas):
        gol = int(input(f'  Quantos gols na partida {c}? '))
        aproveitamento.append(gol)
        s += gol
    futebol['gols'] = aproveitamento[:]
    aproveitamento.clear()
    futebol['total'] = s
    todos.append(futebol.copy())
    futebol.clear()
    s = 0
    continuar = str(input('Deseja continuar[S/N]? ')).upper().strip()[0]
    if continuar not in 'NS':
        continuar = str(input('Não identifiquei a resposta... Deseja continuar [S/N]? ')).strip().upper()[0]
    if continuar == 'N':
        break
    print('=-'*40)
print(f'{"cod":>5}  {"nome":<20}{"gols":<20}{"total":<20}')
for c, v in enumerate(todos):
    print(f'{c:>5}  ', end='')
    for d in v.values():
        print(f'{str(d):<20}',end='')
    print()
print('=-'*40)
while True:
    n = int(input('Qual jogar você quer analisar[999 para parar]? '))
    if n == 999:
        break
    if n >= len(todos):
            n = int(input('Não achamos esse código, digite novamente: '))
    else: 
        print(f'\nLevantamento de dados do jogador {todos[n]["nome"]}:') 
        for i, v in enumerate(todos[n]['gols']):
            print(f'        No jogo {i + 1} ele fez {v} gols.')
print('\n<<<VOLTE SEMPRE>>>')