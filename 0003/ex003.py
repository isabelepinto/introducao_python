#fatiamento
frase = "Bom dia "
print(frase)
print(frase[4])
print(frase[4:7])

teste = "Curso em Vídeo Python"
print(teste[9:21])
print(teste[:9])
print(teste[15:])
#fatiamento pulando de dois em dois
print(teste[9:21:2])
print(teste[::2])

#análise
print(len(teste))
print(teste.count("o"))
print(teste.find("deo"))

#tranformacao
print(teste.replace("Python","CSharp"))

#upper,lower,capitalize,title
frase2 = "bom DIA, hoje o SOL está MUITO BOnitO"
print(frase2)
print(frase2.lower())
print(frase2.upper())
print(frase2.capitalize())
print(frase2.title())

#strip
frase3 = "          bom dia, pra voce    "
print(frase3)
print(frase3.strip())
print(frase3.lstrip())
print(frase3.rstrip())

#split
print(frase3.split())

#join
print("-".join(frase3))