from lib import interfaces
from time import sleep

while True:
    resposta = interfaces.menu(['VISUALIZAR PESSOAS CADASTRADAS',
                                'CADASTRAR NOVO USUÁRIO', 'SAIR DO SISTEMA'])
    print()
    if resposta == 1:
        interfaces.cabecalho('PESSOAS CADASTRADAS')
    elif resposta == 2:
        interfaces.cabecalho('NOVO CADASTRO')
    elif resposta == 3:
        interfaces.cabecalho('Saindo do sistema... até logo!')
        break
    else:
        print('\033[31mERRO. Digite uma opção válida.\033[m')
    sleep(2)
