from datetime import date
ano = int(input("Digite o ano do seu nascimento: "))
now = date.today().year
idade = now - ano
if idade > 18:
    print(f"Já passaram {idade - 18} anos do tempo de alistamento.")
elif idade < 18:
    print(f"Ainda não chegou na idade para alistamento. Faltam {18 - idade} anos.")
else:
    print("Já está na idade de se alistar.")