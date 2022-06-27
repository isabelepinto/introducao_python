#Dicionários:
pessoas = {'nome' : 'Thomas', 'sexo' : 'M', 'idade' : 25}
print(f'\nO {pessoas["nome"]} tem {pessoas["idade"]} anos de idade.')
print()
print('=*' * 20)
print(f'As Keys são: {pessoas.keys()}')
print(f'Os values são: {pessoas.values()}')
print(f'Os itens são as Keys e os values: {pessoas.items()}')
print()
print('=*' * 20)

#Para imprimir editado podemos usar laços de repetição:
for k in pessoas.keys():
    print(k)
print()
print('=*' * 20)
for v in pessoas.values():
    print(v)
print()
print('=*' * 20)
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()
print('=*' * 20)

#Para deletar um item usamos o del:
del pessoas['sexo']
print(pessoas) #Veja que só teremos as chaves 'nome' e 'idade'.
print()
print('=*' * 20)

#Para adicionar um elemento usamos:
pessoas['peso'] = 83.5
print(pessoas) #Irá aparecer a nova chave 'peso'.
print()
print('=*' * 20)

#Para modificar um valor:
pessoas['nome'] = 'Marcelo'
print(pessoas)
print()
print('=*' * 20)

#Colocando Dicionários dentro de uma lista:
estado1 = {'uf' : 'Piauí', 'sigla' : 'PI'}
estado2 = {'uf' : 'São Paulo', 'sigla' : 'SP'}
estados = list()
estados.append(estado1)
estados.append(estado2)
print(f'Os estados da minha lista são: {estados}')

#Para pegar um input de dicionários e adicionar em uma lista devemos usar o lista.append(dicionario.copy()):
estado = dict()
brasil = list()
for v in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Qual a sigla? '))
    brasil.append(estado.copy())
print(brasil)

#Para ordenar dicionários em posições do maior colocado para o menor:
#from operator import itemgetter #precisamos importar esse dicionário
#ranking = sorted(sorteio.items(), key=itemgetter(1), reverse=True) #depois usar essa funcionalidade do sorted