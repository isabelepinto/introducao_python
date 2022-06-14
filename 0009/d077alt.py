palavras = ('Aprender', 'Programar', 'LINGUAGEM', 'Python', 'curso', 'gratis', 'estudar', 'PRATICAR', 'TRABALHAR', 'Mercado', 'Programador', 'Futuro')
for p in palavras:
    print(f'\nA palavra {p.upper()} tem as vogais: ', end="")
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=" ")
