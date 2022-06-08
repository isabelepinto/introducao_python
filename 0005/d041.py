from datetime import date
now = date.today().year
ano = int(input("Digite o ano de seu nascimento: "))
idade = now - ano
print(f"Você tem {idade} anos de idade.")
if idade <= 9:
    print("Você está na categoria MIRIM.")
elif idade <= 14:
    print("Você está na categoria INFANTIL.")
elif idade <= 19:
    print("Você está na categoria JÚNIOR.")
elif idade <= 25:
    print("Você está na categoria SÊNIOR.")
else:
    print("Você está na categoria MASTER.")