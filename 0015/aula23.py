# Erros e exceções
# Erros de sintaxe não estão inclusos, pois o compilador não vai entender
# Prever os erros semânticos do usuário
# Sempre melhorar a experiência do usuário
# try(o que poderia dar problema) and except (se falhar) // else (deu certo) // finally (certo/falha)
# todo try pode ter mais de uma exception - isso facilita a personalização da mensagem para o usuário

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except:  # podemos usar 'except Exception as erro:' e na resposta colocar a variável "erro.__class__"
    print('Infelizmente tivemos um problema :(')
else:
    print(f'O resultado dessa divisão é {r}')
finally:
    print('\nMuito obrigada, volte sempre!\n')
