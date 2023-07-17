opção=0

n1=int(input('N1: '))
n2=int(input('N2: '))

while opção!=5:
    cont=-1
    lista = ('somar', 'multiplicar', 'maior', 'novos números', 'sair do programa')
    print('\nEscolha a operação')

    for c in range(1,6,1):
        cont=cont+1
        print(f'{c} {lista[cont]}')
    opção=int(input('-> '))
    if opção==1:
        print(f'\nA soma de {n1} e {n2} é {n1+n2}')
    elif opção==2:
        print(f'\nO produto de {n1} e {n2} é igual a {n1*n2}')
    elif opção==3:
        if n1>n2:
            maior=n1
        else: maior=n2
        print(f'\nEntre {n1} e {n2}, o maior é {maior}')
    elif opção==4:
        print('\nNOVOS NÚMEROS')
        n1 = int(input('N1: '))
        n2 = int(input('N2: '))








