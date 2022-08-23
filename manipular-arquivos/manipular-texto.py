import shutil


def escrever_texto(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'w')
    arquivo.write(texto)
    arquivo.close()


def adicionar_texto(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()


def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)


def media_aluno(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    alunos_notas = arquivo.read()
    alunos_notas = alunos_notas.split('\n')
    resultado = {}
    for i in alunos_notas:
        dados = i.split(',')
        media = (float(dados[1]) + float(dados[2]) + float(dados[3]))/3
        lista_media = f'{media:.2f}'
        resultado[dados[0]] = lista_media
    print(resultado)


def copiar_arquivo(nome_arquivo):
    shutil.copy(
        nome_arquivo, 'C:/Users/bebel/OneDrive/Attachments/Documents/programacao/introducao_python/copia/notas_teste.txt')


def mover_arquivo(nome_arquivo):
    shutil.move(
        nome_arquivo, 'C:/Users/bebel/OneDrive/Attachments/Documents/programacao/introducao_python')


if __name__ == '__main__':
    #escrever_texto('primeira linha.\n')
    #adicionar_texto('segunda linha.\n')
    #adicionar_texto('terceira linha.\n')
    # ler_arquivo('texto1.txt')
    #adicionar_texto('notas.txt', texto)
    # media_aluno('notas.txt')
    # copiar_arquivo('notas.txt')
    mover_arquivo('texto1.txt')
