n = str(input('Digite aqui sua expressão: '))
lista = list()
for c in n:
    if c == '(':
        lista.append('(')
    elif c == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('A expressão está correta.')
else: 
    print('A expressão está errada!')
