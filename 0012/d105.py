def notas(* num, sit=False):
    """
    -> Função para armazenar e calcular qual quantidade de notas, a maior e menor nota, a média, e, se a situção for True, colocar o status da média, tudo isso em um dicionário.
    :num: as notas que serão adicionadas (aceitam várias)
    :sit: a situação da média final, se True irá ser adicionada ao dicionário
    :return: o retorno do dicionário com todos os dados
    """
    dados = {}
    dados['total'] = len(num)
    sorted(num)
    dados['maior'] = num[-1]
    dados['menor'] = num[0]
    media = sum(num) / len(num)
    dados['média'] = f'{media:.2f}'
            
    if sit:
        if media <= 5:
            dados['situação'] = 'RUIM'
        elif 7 > media > 5:
            dados['situação'] = 'RAZOÁVEL'
        else:
            dados['situação'] = 'BOA'
        return dados
    return dados
    

#Programa principal:  
resp = notas(9.5, 4, 3.2, 9, 10, sit=True)
print(resp)
