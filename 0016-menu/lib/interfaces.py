def leiaInt(n):
    while True:
        try:
            n = int(input(n))
        except (ValueError, TypeError):
            print(
                '\033[31mO valor digitado é inválido! Tente novamente... \033[m')
            continue
        except (KeyboardInterrupt):
            print(
                '\033[31mO usuário preferiu não digitar esse número\033[m')
            return 0
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for i in lista:
        print(f'\033[34m0{c} - {i}\033[m ')
        c += 1
    print(linha())
    opc = leiaInt('Digite sua opção: ')
    return opc
