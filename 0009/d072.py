numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 
'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 
'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if -1 < n < 21:
            break
        n = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    print(f'O número que você escolheu foi o {numeros[n]}')
    continuar = str(input("Deseja continuar? [S/N]")).upper().split()[0]
    if continuar == "N":
        break
