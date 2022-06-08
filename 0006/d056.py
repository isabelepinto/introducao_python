soma = 0
maior = 0
fmenor = 0
nomeMaior = ""
for i in range(1, 5):
    print(f"**--- PESSOA Nº {i} ---**")
    nome = str(input("Seu nome: ")).upper()
    idade = int(input("Sua idade: "))
    sexo = str(input("Sexo(M/F): ")).upper()
    soma += idade
    if sexo == "F" and idade < 20:
        fmenor += 1
    
    if sexo == "M" and idade > maior:
        maior = idade
        nomeMaior = nome
        
print(f"A média da idade das quatro pessoas é {soma / 4}")
print(f"O número de pessoas do sexo feminino menor de 20 anos é de {fmenor} pessoas.")
print(f"O nome do homem mais velho é {nomeMaior} e ele tem {maior} anos de idade.")