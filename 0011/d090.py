snoopy = {}

snoopy['nome'] = str(input('Digite seu nome: ')).capitalize()
while True:
    snoopy['média'] = float(input('Digite sua média: '))
    if snoopy['média'] > 10 or snoopy['média'] < 0:
        print('Por favor, digite novamente sua média entre 0 e 10.')
    else:
        break
if snoopy['média'] >= 7:
    snoopy['situação'] = 'aprovado'
else:
    snoopy['situação'] = 'reprovado'
print()
print('*=' * 30)
for k, v in snoopy.items():
    print(f'- {k} é igual a {v}')
