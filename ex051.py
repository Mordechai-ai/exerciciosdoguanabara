termo1=int(input('Primeiro termo da PA: '))
razao=int(input('Razão da PA: '))
decimo=termo1+(11-1)*razao
print('\033[4:31mDEZ PRIMEIROS TERMOS DA PROGRESSÃO\033[m')
for c in range (termo1,decimo,razao):
        print(f'{c} ',end='')
