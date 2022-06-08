sexo = str(input("Digite seu sexo [M/F]: ")).strip().upper()[0]
while sexo not in "MmFf":
    print("Você digitou errado. \nEscolha F ou M")
    sexo = str(input("Digite novamente seu sexo[M/F]: ")).strip().upper()[0]
if sexo in "Ff":
    print("Você é do sexo feminino.")
else:
    print("Você é do sexo masculino.")