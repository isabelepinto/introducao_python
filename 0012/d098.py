from time import sleep
def contagem(inicio, fim, passo):
    """
    -> Faz uma contagem e mostra na tela, sendo:
    para inicio: o inteiro que inicia a contagem
    para fim: o inteiro que finaliza a contagem
    para passo: o passo em que será contado do inicio ao fim
    return: sem retorno
    """
    if passo < 0:
        passo = -passo
    if passo == 0:
        passo = 1
        print('Não podemos usar o passo 0, usaremos o passo padrão...')
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
    if inicio < fim:
        for i in range(inicio, (fim + 1), passo):
            print(f'{i}', end=' ', flush=True)
            sleep(.5)
        print('FIM', end=' ')
        print()
    else:
        for i in range(inicio, (fim + 1), -passo):
            print(f'{i}', end=' ', flush=True)
            sleep(.5)
        print('FIM', end=' ')
        print()

#Programa principal:    
help(contagem) 
contagem(1, 10, 1)
contagem(10, 0, 2)
print('Agora é sua vez de personalizar a contagem: ')
contagem(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))
