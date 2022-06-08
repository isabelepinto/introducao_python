nome = input("Digite seu nome completo: ")
print(f"Em maiusculas: {nome.upper()}")
print(f"Em minusculas: {nome.lower()}")
espaco = nome.count(" ")
nletras = (len(nome)) - espaco
print(f"O numero de letras totais sem considerar o espaco é: {nletras}")
primeiro_nome = nome.split()
print(f"Seu primeiro nome tem: {len(primeiro_nome[0])} letras")