n = c = s = 0
while n != 999:
    n = int(input("Digite um número n: "))
    c += 1
    s += n
    print("Para encerrar o programa digite 999 ou ...")
    if n == 999:
        c = c - 1
        s = s - 999
print(f" Você solicitou {c} números e a soma desses números foi {s}.")