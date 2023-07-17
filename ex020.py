import random
nome1=str(input('Nome do aluno 1: '))
nome2=str(input('Nome do aluno 2: '))
nome3=str(input('Nome do aluno 3: '))
nome4=str(input('Nome do aluno 4: '))
lista= (nome1,nome2,nome3,nome4)
sorteados=(random.sample(lista,4))
print(f'1ºApresentação: {sorteados[0]}')
print(f'2º Apresentação: {sorteados[1]}')
print(f'3º Apresentação: {sorteados[2]}')
print(f'4º Apresentação: {sorteados[3]}')

