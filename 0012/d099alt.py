from time import sleep
#Função para analisar os dados e fazer desenpacotamento 
def maior(* num):
        print('=-' * 30)
        sleep(1)
        print(f'\nAnalisando os valores passados...')
        m = c = 0
        for n in num:
            print(f'{n} ',end='', flush=True)
            sleep(.5)
            if c == 0:
                m = n
            else:
                if n > m:
                    m = n
            c += 1
        print(f'\nForam informados {len(num)} valores. Sendo o maior valor informado o {m}.')
        


#Programa principal
maior(2, 9, 4, 6, 3, 8)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
