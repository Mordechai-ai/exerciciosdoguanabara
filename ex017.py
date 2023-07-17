import math
cateto1=float(input('Qual a medida do cateto 1 em cm? '))
cateto2=float(input('Qual a medida do cateto2 em cm? '))
hipotenusa=(math.hypot(cateto1,cateto2))
print(f'A medida da hipotenusa é: {hipotenusa:.2f} cm')
