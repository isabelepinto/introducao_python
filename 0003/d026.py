frase = input("Escreva uma frase: ")
letra_a = frase.lower().count("a")
primeiro_a = frase.lower().find("a")
print(f"A letra a aparece {letra_a} vezes")
print(f"A letra a aparece a primeira vez na posicao {primeiro_a}")