#Criar função que leia apenas números inteiros. Caso não seja um número inteiro, ela apresentará mensagem de erro e continuará rodando.

def leiaInt(n):
    """
    -> Ler um input qualquer e validar se é um inteiro, se não for, o programa irá repetir o input até ser válido
    :n: número a ser validado
    :return: retorna o valor n somente após ser validado como inteiro
    """
    if n.isdigit():
        return n
    else: 
        while True:
            print('\nERRO! Só podemos validar números inteiros...\n')
            n = input('Digite um número inteiro: ')
            if n.isdigit():
                break
        return n
            
            
num = leiaInt(input('Digite um número: '))
print(f'Você acabou de digitar o número {num}')