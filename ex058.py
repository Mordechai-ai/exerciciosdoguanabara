import random
tentativas=0
numero=0
sorteado=12

while numero != sorteado:
    numero = int(input('Aposte em um número entre 1 e 10 - '))
    sorteado = random.randint(1, 10)
    tentativas=tentativas+1

    if numero==sorteado:
        print('PARABÉNS, VOCÊ ACERTOU!!!')
    else:
        print('VOCÊ ERROU HAHAHA.',end='')
        print(f' O número era {sorteado}')
print('Jogo Terminado')
print(f'Você teve de tentar {tentativas} antes de acertar ')
