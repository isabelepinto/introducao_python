# Manipulando Strings
## Fatiamento
ex.:
```frase = "Bom dia "```
```print(frase)``` - irá imprimir a frase inteira
Porém, se escolhermos um caractere através de: ```frase[4]``` - irá ser impresso o caractere "d"
Tmabém podemos escolher o inicio e o fim dos caracteres com: ```frase[4:7]``` e será impresso "dia"
Também podemos colocar ```frase[4:7:2]``` - e será impresso pulando de 2 em dois: "da"

## Análise de Strings
1. Vamos utilizar o ```len(frase)``` pra sabermos o comprimento da string
2. Usamos tb o comando ```frase.count("o")``` e isso contará quantas vezes existem a letra "o" dentro da string
3. Outro comando é o ```frase.find("bom")``` e ele irá mostrar onde está esse trecho de string

## Transformacao 
Podemos usar o ```frase.replace("dia","almoco")``` para alterar a palavra na string
Podemos usar ```frase.lower()``` ou ```frase.upper()``` para deixar tudo em minusculas ou em maiusculas
Também ha o ```frase.capitalize()``` e deixara a primeira palavra da frase em maiuscula
Ja o ```frase.title()``` e deixara toda as iniciais maiúsculas
Temos tabem o ```frase.strip()``` que vai remover os espacos colocados no inicio e no final da frase desnecessariamente
E existe a variacao de ```frase.lstrip()``` para o left e ```frase.rstrip()``` para o right

## Divisao
Para isso usamos o split e suas variacoes
Por padrao, o ```frase.split()``` fará a divisao usando os espacos, porem isso pode ser alterado.

## Juncao
Para isso usamos o join
ex.: ```"-".join(frase)```