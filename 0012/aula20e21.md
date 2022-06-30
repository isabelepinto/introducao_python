# Aula Funções:

## Interactive help
- Para conseguir ajuda interativa em Python podemos usar a função ''' help() '''.
- Para isso, digitamos help() no console do PyCharm.

## Docstrings
- Se eu crio uma função e eu quero documentá-la para que outras pessoas saibam a funcionalidade e possam chamá-la no '''help()''', eu tenho que usar o docstrings.
- Para isso, logo na linha abaixo da inicialização da função def, colocamos três aspas duplas, digitamos a documentação e fechamos com três aspas duplas em seguida.

## Argumentos opcionais
- Podemos criar parêmetros opcionais em nossas funções.
- Ex.: em uma função para somar 3 valores (a,b,c), se colocarmos (a=0, b=0, c=0) então, ao chamar a função, se não colocarmos os 3 parâmetros, a função irá entender que o parâmetro faltante é 0.

## Escopo de variáveis
- Possuímos o escopo global e o escopo local.
- A variável no escopo global, pode ser chamada dentro da função ou dentro do programa principal.
- Já uma variável com escopo local, só pode ser chamada em uma área específica, por ex.: dentro da função que ela foi criada. Ela também não consegue alterar o valor da variável com escopo global.
- No Pyhton podemos ter uma variável local e uma variável global com o mesmo nome, porém serão armazenadas em lugares diferentes na memória, podendo assim terem valores diferentes sem um alterar o outro.

## Retorno de resultados
- Na função podemos somente chamar a palavra '''return''' para armazenar o resultado da função, sem a necessidade de dar print ou ver no console, podendo colocá-la em uma variável.