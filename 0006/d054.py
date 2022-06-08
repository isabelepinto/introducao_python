from datetime import date
menor = 0
maior = 0
now = date.today().year
for i in range(1, 8):
    ano = int(input(f"Em que ano a {i}ª pessoa nasceu? "))
    idade = now - ano
    if idade < 18:
        menor += 1
    else:
        maior += 1
print(f"Segundo nosso sistema, das 7 pessoas entrevistadas, {menor} são menores de idade e {maior} são maiores de idade.")