import random
sorteado=random.randint(1,5)
numero=int(input('Aposte em um número entre 1 e 5 - '))
if numero==sorteado:
    print('PARABÉNS, VOCÊ ACERTOU!!!')
else:
    print('VOCÊ ERROU HAHAHA.',end='')
    print(f' O número era {sorteado}')
print('Sorteio Terminado')