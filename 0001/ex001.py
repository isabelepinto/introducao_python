nome = str(input("Qual é o seu nome? "))
print(f"Prazer em te conhecer, {nome}!")
#Para centralizar um nome, podemos usar o ^ e em seguida o número de caracteres
print(f"Prazer em te conhecer, {nome:^20}!")

n1 = int(input("Digite aqui o n1: "))
n2 = int (input("Digite aqui o n2: "))
soma = n1 + n2
subt = n1 - n2
divisao = n1 / n2
resto = n1 % n2
multip = n1 * n2
expon = n1 ** n2
print(f"A soma é {soma}, a subtracao é {subt}, a divisao é {divisao} e o resto é {resto}, a multiplicacao é {multip} e o potenciacao fica {expon}. Correto? ")
