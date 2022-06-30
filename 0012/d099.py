from time import sleep
#Função para analisar os dados e fazer desenpacotamento 
def maior(* num):
        print('=-' * 30)
        print(f'\nAnalisando os valores passados...')
        sleep(1)
        if len(num) == 0:
                print('Não há número a ser analisado.')
        else:
                print(f'{(num)}', flush=True)
                sleep(1)
                print(f'\nForam informados {len(num)} números ao todo. O maior valor informado foi {max(num)}.')


#Programa principal
maior(2, 9, 4, 6, 3, 8)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
