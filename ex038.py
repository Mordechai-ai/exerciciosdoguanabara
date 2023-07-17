n1=int(input('N1: '))
n2=int(input('N2: '))
if n1>n2:
    print(f'O primeiro valor {n1} é maior')
elif n1<n2:
    print(f'O segundo valor {n2} é maior ')
elif n1 == n2:
    print(f'Não existe valor maior, os dois são iguais')
