final = []
dados = []
nomes = []
notas = []
medias = []
while True:
    nomes.append(str(input('Digite seu nome: ')).capitalize().strip())
    dados.append(nomes[:])
    notas.append(float(input('Digite sua 1ª nota: ')))
    notas.append(float(input('Digite sua 2ª nota: ')))
    media = (notas[0] + notas[1])/2
    medias.append(media)
    dados.append(notas[:])
    final.append(dados[:])
    continuar = str(input('Deseja continuar?[S/N]')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Não entendi. Deseja continuar?[S/N]')).upper().strip()[0]
    if continuar == 'N':
        break
    nomes.clear()
    notas.clear()
    dados.clear()
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 30)
for i in range(0, len(final)):
    print(f'{i:<4}{final[i][0][0]:<10}{medias[i]:>8.1f}')

print('-' * 30)
while True:
    n = int(input('Mostrar notas de que aluno?(999 interrompe) '))
    if n == 999:
        print('Finalizando...')
        break 
    if n < len(final): 
        print(f'As notas de {final[n][0][0]} são {final[n][1][0]} e {final[n][1][1]}')