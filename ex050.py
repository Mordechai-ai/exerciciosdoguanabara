soma=0
for c in range (1,7):
    n1=int(input(f'N{c}: '))
    if n1%2==0:
        soma=soma+c
print(f'A soma somente dos números pares dá {soma}')