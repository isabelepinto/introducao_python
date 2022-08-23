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


def leiaReal(n):
    while True:
        try:
            n = float(input(n).replace(',', '.'))
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


num = leiaInt('Digite um número inteiro: ')
print(f'O valor digitado foi {num}')
numReal = leiaReal('Digite um número real: ')
print(f'O valor digitado foi {numReal}')
