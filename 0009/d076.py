listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-'*47)
print(f'{"LISTAGEM DE PREÇOS":^43}')
print('-'*47)
for i in range(0, len(listagem), 2):
    print(f'{listagem[i]:.<36} R$ {listagem[i+1]:>6.2f}')
print('-'*47)
