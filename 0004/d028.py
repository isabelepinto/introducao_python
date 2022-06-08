from random import choice
from time import sleep
n = [0,1,2,3,4,5]
aleatorio = choice(n)
print("-=-" * 20)
print("Vou pensar em um número entre 0 e 5... tente advinhar!")
print("-=-" * 20)
advinha = int(input("E aí? Em qual numero eu pensei? "))
print("PROCESSANDO...")
sleep(2)
if aleatorio == advinha:
    print("Voce venceu!")
else:
    print(f"Voce perdeu, o numero sorteado foi o {aleatorio}")