print("Avaliando empréstimo:")
print("-" * 25 )
valor_casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite seu salário atual: "))
anos = int(input("Digite em quantos anos deseja parcelar: "))
parcela = valor_casa / (anos * 12)
if parcela <= salario * 0.3:
    print("Parabéns. Seu emprestimo foi aprovado!")
    print(f"Sua parcela é de R${parcela:.2f} reais mensal.")
else:
    print("Infelizmente seu empréstimo não foi aprovado...")