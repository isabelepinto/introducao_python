frase = str(input("Escreva uma frase: ")).strip().lower()
print(f"A letra a aparece {frase.count('a')} vezes")
print(f"A letra a aparece a primeira vez na posicao {frase.find('a') + 1}")
print(f"A letra a aparece a ultima vez na posicao {frase.rfind('a') + 1}")