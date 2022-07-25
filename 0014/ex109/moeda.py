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

