frase = str(input("Digite uma frase: ")).strip().lower()
separa = frase.split(" ")
junta = "".join(separa)
inverso = ""
for letra in range(len(junta) - 1, -1, -1):
    inverso += junta[letra]
print(f"O inverso de {junta} é: {inverso}.")
if inverso == junta:
    print("Eles são palíndromos.")
else:
    print("Eles não são palíndromos.")