# para criar ou abrir arquivos usamos o 'open()'
# usamos o 'w' para escrever e o 'a' para adiconar novo texto sem apagar o anterior
arquivo = open('teste.txt', 'a')
# após a criação do arquivo, se rodarmos o código novamente, não será criada cópia do arquivo

# para escrever usamos 'arquivo.write()'
arquivo.write('\nEssa é a terceira linha')
# para fechar o arquivo escrevemos 'arquivo.close()'
arquivo.close()

# para ler um arquivo usamos:
arquivo = open('teste.txt', 'r')
texto = arquivo.read()
print(texto)

# para copiar um arquivo precisamos importar a biblioteca shutil
# colocamos o nome do arquivo e o diretório em que queremos copiar
