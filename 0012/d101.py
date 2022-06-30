# Criar um programa para ler o ano de nascimento de uma pessoa e dizer se ela tem voto obrigatório, opcional ou negado.
# Considerar que até os 15 o voto é negado. Dos 16 aos 18 o voto é opcional, bem como a partir dos 65 anos.

def voto(ano):
    """
    Função -> recebe o ano de nascimento do usuário
    para idade: calcula a partir do ano atual do sistema, precisa importar a data da biblioteca
    return: string com a situação do voto(obrigatório, opcional ou negado)
    """
    from datetime import datetime
    idade = datetime.now().year - ano
    if idade < 16:
        return print('Voto negado, você tem menos de 16 anos.')
    elif idade <= 18 or idade > 65:
        return print(f'Voto opcional, você tem {idade} anos, por isso não precisa votar.')
    else:
        return print(f'Você tem {idade} anos, por isso, seu voto é obrigatório.')
    
    
# Programa principal
nome = input('Seja muito bem vinda(o)! \nDigite seu nome: ').strip().capitalize()
voto(int(input(f'Olá, {nome}. \nPara verificar sua situação de voto, digite seu ano de nascimento: ')))