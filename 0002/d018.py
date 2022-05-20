import math
angulo = int(input("Digite o angulo: "))
cos = math.cos(math.radians(angulo))
seno = math.sin(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print(f"O seno do angulo {angulo} é {seno:.2f}, seu cosseno é {cos:.2f} e sua tangente é {tan:.2f}")