n = int(input("Digite um numero para converter: "))
print("Escolha o número: \n1 - para binário; \n2 - para octal; \n3 - para hexadecimal;")
converter = int(input(""))
if converter == 1:
    print(f"O numero {n} convertido para binário é: {bin(n)[2:]}")
elif converter == 2:
    print(f"O numero {n} convertido para octal é: {oct(n)[2:]}")
elif converter == 3:
    print(f"O numero {n} convertido para hexadecimal é: {hex(n)[2:]}")
else:
    print("O número digitado é inválido.")