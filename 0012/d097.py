#criar função que as linhas se adaptem ao tamanho da mensagem
def escreva(msg):
    print('~' * (len(msg) + 4))
    print(f'  {msg}')
    print('~' * (len(msg) + 4))


#Programa principal:
escreva(str(input('Digite sua mensagem: ')))