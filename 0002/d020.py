from random import shuffle, sample
a1 = input("Digite seu nome, aluno 1: ")
a2 = input("Digite seu nome, aluno 2: ")
a3 = input("Digite seu nome, aluno 3: ")
a4 = input("Digite seu nome, aluno 4: ")
a = [a1, a2, a3, a4]
shuffle(a)
print(f"A ordem de apresentacao será:\n {a}")
