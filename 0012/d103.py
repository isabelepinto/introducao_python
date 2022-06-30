def ficha(n='', g=''):
    """
    -> Função para coletar nome e quantidade de gols de um jogador
    :para n: o nome do jogador
    :para g: a quantidade de gols
    :return: sem return
    """
    print('-=' * 30)
    print('FICHA TÉCNICA\n')
    n = str(input('Digite seu nome: ')).strip().capitalize()
    g = str(input('Digite o número de gols: ')).strip()
    if n == '':
        n = '<desconhecido>'
    if g.isnumeric():
        g = int(g)
    else:
        g = 0
    print(f'O jogador {n} fez {g} gols.')


ficha()
