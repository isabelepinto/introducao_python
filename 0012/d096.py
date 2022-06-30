#função para calcular a área de um terreno:
def area(a, b):
    x = a * b
    print(f'A área de um terreno {a:.1f} x {b:.1f} é de {x} m²')


#Programa principal:
print('Controle de Terrenos:')
area(float(input('LARGURA (m): ')), float(input('COMPRIMENTO (m): ')))