arquivo = []
soma_idades = 0
mulheres = []
while True:
    nome = str(input('Digite seu nome: '))
    sexo = str(input('Digite seu sexo: ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo não identificado... Digite seu sexo: ')).strip().upper()[0]
    if sexo == 'F':
        mulheres.append(nome)
    idade = int(input('Digite sua idade: '))
    soma_idades += idade
    continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    dados = {}
    dados['nome'] = nome
    dados['sexo'] = sexo
    dados['idade'] = idade
    arquivo.append(dados)
    if continuar not in 'NS':
        continuar = str(input('Não identifiquei a resposta... Deseja continuar [S/N]? ')).strip().upper()[0]
    if continuar == 'N':
        break
media = soma_idades / len(arquivo)
print(f'O grupo tem {len(arquivo)} pessoas cadastradas. \nA média de idade é de {media:5.2f} \nAs mulheres cadastradas foram {mulheres}.')
print('As pessoas que têm idade acima da média são: ', end='')
for p in arquivo:
    if p['idade'] >= media:
        print(p['nome'], end=' ')
print()
print('>>>>ENCERRADO')
