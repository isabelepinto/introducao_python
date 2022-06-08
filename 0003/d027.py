nome = input("Digite seu nome completo: ")
lista = nome.split()
nfinal = len(lista) - 1
print(f"Seu primeiro nome é: {lista[0]}")
print(f"Seu último nome é: {lista[nfinal]}")