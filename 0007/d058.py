from random import choice
count = 0
n = [0,1,2,3,4,5,6,7,8,9,10]
pc = choice(n)
adivinha = int(input("Tente adivinhar em que número eu estou pensando... "))
while pc != adivinha:
    adivinha = int(input("Tente novamente, você errou... "))
    count += 1
print(f"Muito bem, você acertou. Eu estava pensando no número {pc}")
print(f"Você precisou tentar {count + 1} vezes para adivinhar.")