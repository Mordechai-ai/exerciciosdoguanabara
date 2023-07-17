numero=int(input('Digite um número: '))

x=0
for c in range (numero,0,-1):
    if numero%c==0:
        x=x+1
if x==2:
    print(f'O número {numero} é um número primo')
else:
    print(f'O número {numero} não é um número primo')