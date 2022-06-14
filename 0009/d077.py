palavras = ('Aprender', 'Programar', 'LINGUAGEM', 'Python', 'curso', 'gratis', 'estudar', 'PRATICAR', 'TRABALHAR', 'Mercado', 'Programador', 'Futuro')
for palavra in palavras:
    print(f'Na palavra {palavra.upper()} temos a vogal: ', end=" ")
    a = palavra.upper().count('A')
    if a > 0:
        print('a ' * a, end=" ")
    e = palavra.upper().count('E')
    if e > 0:
        print('e ' * e, end=" ")
    i = palavra.upper().count('I')
    if i > 0:
        print('i ' * i, end=" ")
    o = palavra.upper().count('O')
    if o > 0:
        print('o ' * o, end=" ")
    u = palavra.upper().count('U')
    if u > 0:
        print('u ' * u, end=" ")
    print("")