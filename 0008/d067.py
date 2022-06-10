x = 0
while True:
    n = int(input('Digite o número para gerar a tabuada: '))
    print("Para encerrar, digite um número negativo.")
    if n < 0:
            break
    print('-' * 20)  
    x = 0  
    while x < 11:
        print(f'{n} x {x}  = {n * x}')
        x += 1
    print('-' * 20)    
print(f"Você digitou {n} e a sessão foi encerrada. Volte sempre!")        
