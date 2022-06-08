salario = float(input("Qual o valor do seu salario? "))
aumento10 = salario * 1.10
aumento15 = salario * 1.15
if salario > 1250:
    print(f"O valor do seu novo salario é de R$ {aumento10:.2f}.")
else:
    print(f"O valor do seu novo salário é de R$ {aumento15:.2f}.")