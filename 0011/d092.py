from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: ')).capitalize().strip()
nascimento = int(input('Ano de nascimento: '))
idade = datetime.now().year - nascimento
dados['idade'] = int(idade)
dados['ctps'] = int(input('Carteira de Trabalho[se não tem, digite 0]: '))
if dados['ctps'] == 0:
    for k, v in dados.items():
        print(f'{k} tem valor {v}')
    print('Você precisa possuir uma Carteira de Trabalho para continuar...')
else:
    dados['ano'] = int(input('Qual o ano de contratação? '))
    dados['salario'] = float(input('Qual seu salário mensal? '))
    falta = idade + (35 - (datetime.now().year - dados['ano']))
    dados['aposentar'] = int(falta)
    for k, v in dados.items():
        print(f'{k} tem valor {v}')
