def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número:
    :para n: O número a ser fatorado.
    :para show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial do número n. 
    """
    f = 1
    for i in range(n, 0, -1):
        f = f * i
        if show:
            print(i, end="")
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    return f
    
    
#Programa principal:    
print(fatorial(5, True))