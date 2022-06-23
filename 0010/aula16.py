'''
Para criar listas, podemos colocar compras = ['mochila', 'lapis', 'folha A4'] ou também podemos criar uma LISTA VAZIA com o comando compras = list().
Se quisermos adicionar um item na lista, basta usar o comando compras.append('papel') e ele vai adicionar ao final da lista. 
Mas, para adicionar numa posição específica, temos que usar o comando insert: compras.insert(2, 'borracha') e ele vai adicionar na posição 2.
Podemos também ordenar uma lista com o compras.sort() e para ordenar ao contrário podemos usar o compras.sort(reverse=True).
Para deletar o item de uma lista podemos usar o comando pop: compras.pop() irá deletar o último item, mas, se quisermos deletar um item específico podemos usar o compras.pop(2) e ele apagará o item na posição 2.
Também podemos usar o comando del compras[2] e vai deletar o elemento da posição 2 ou usar o compras.remove('mochila') e vai deletar o item entre parênteses.

#MUITO IMPORTANTE:
Para copiarmos uma lista para outra variável NÃO podemos apenas usar b = a. Temos que usar: b = a[:], aí sim iremos copiar os valores de a em b
'''
a = list() #criando uma lista vazia
a.append(3) #adicionando itens à essa lista
a.append(6)
a.append(45)
b = a[:] #copiando os itens de a em b 
a.append(22)
a.append(2)
print(f'Lista A:{a}, Lista B:{b}') #aqui, as alterações feitas depois de termos copiado os itens de a em b não afetarão b
b.insert(2, 55)
print(f'Lista B:{b}')
for c, v in enumerate(a):
    print(f'Na posição {c} encontrei o número {v}')
del a[2]
a.pop(0)
print(f'Lista A:{a}')

#Podemos adicionar uma lista dentro de outra em um único item, po exemplo:
dados1 = ['Fernando', 32]
dados2 = ['Joana', 43]
exemplo = list()
exemplo.append(dados1)
print(exemplo)
exemplo.append(dados2)
print(exemplo)
print(exemplo[0][1])

#Para recebermos dados de listas dentro de listas podemos:
dados = []
galera = []
for c in range(0,3):
    dados.append(str(input('Digite seu nome: ')))
    dados.append(int(input('Digite sua idade: ')))
    galera.append(dados[:])
    dados.clear()
print(galera)
