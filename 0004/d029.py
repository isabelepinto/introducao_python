velocidade = float(input("Em qual velocidade voce está dirigindo? "))
multa = 7 * (velocidade - 80)
if velocidade > 80:
    print(f"A velocidade máxima é de 80km/h... Voce está sendo multado, o valor a pagar é de R$ {multa}")
else:
    print("Muito bem, voce está dentro do limite de velocidade. Tenha um bom dia!")