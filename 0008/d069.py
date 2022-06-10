maiores = menores = homem =  0
while True:
    idade = int(input("Qual sua idade? "))
    if idade > 18:
        maiores += 1
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Qual seu sexo?[M/F] ")).upper().strip()[0]
    if sexo in "Mm":
        homem += 1
    if sexo in "Ff" and idade < 20:
        menores += 1
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Deseja continuar?[S/N]")).upper().strip()[0]
    if continuar in "Nn":
        break
print(f"{maiores} pessoas tem mais de 18 anos.\n{homem} homens foram cadaastrados.\n{menores} mulheres têm menos de 20 anos.")