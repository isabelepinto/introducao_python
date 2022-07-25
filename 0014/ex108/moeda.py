def metade(n):
    metade = n/2
    return metade


def dobro(n):
    dobro =  n*2
    return dobro



def aumento(n, taxa):
    a = n * (100 + taxa) / 100
    return a


def reduzir(n, taxa):
    r = n * (100 - taxa) / 100
    return n

def moeda(n):
    return f'R${n:8.2f}'.replace('.',',')
