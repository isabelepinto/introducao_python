def moeda(n):
    return f'R${n:8.2f}'.replace('.',',')

def metade(n, mostrar = True):
    metade = n/2
    if mostrar == True:
        return moeda(metade)
    else:
        return metade


def dobro(n, mostrar = True):
    dobro =  n*2
    if mostrar == True:
        return moeda(dobro)
    else:
        return dobro



def aumento(n, taxa, mostrar = True):
    a = n * (100 + taxa) / 100
    if mostrar == True:
        return moeda(a)
    else:
        return a


def reduzir(n, taxa, mostrar = True):
    r = n * (100 - taxa) / 100
    if mostrar == True:
        return moeda(r)
    else:
        return r

def resumo(n = 0, x = 10, y = 5):
    print('-' * 50)
    print('RESUMO DO VALOR'.center(50))
    print('-' * 50)
    print(f'Preço analisado:\t{moeda(n)}')
    print(f'Dobro do preço:\t\t{dobro(n)}')
    print(f'Metade do preço:\t{metade(n)}')
    print(f'Aumento de {x}%:\t\t{aumento(n, x)}')
    print(f'Redução de {y}%:\t\t{reduzir(n, y)}')
    print('-' * 50)
