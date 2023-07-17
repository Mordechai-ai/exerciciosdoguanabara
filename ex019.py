import random
nome1=str(input('Nome do aluno 1: '))
nome2=str(input('Nome do aluno 2: '))
nome3=str(input('Nome do aluno 3: '))
nome4=str(input('Nome do aluno 4: '))
lista= (nome1,nome2,nome3,nome4)
sorteado=(random.randint(0,3))
print(lista[sorteado])
