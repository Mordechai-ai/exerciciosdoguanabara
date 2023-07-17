print('-'*50)
print('VEJA SE A FRASE QUE VC VAI DIGITAR É UM PALÍNDROMO')
print('-'*50)

frase=str(input('\nDigite uma frase: '))
x=frase
frase=frase.replace(' ','')
frase=frase.replace('ó','o')
frase=frase.replace('á','a')
frase=frase.replace('é','e')
frase=frase.replace('í','i')
frase=frase.replace('ú','u')
frase=frase.lower()
caracteres=len(frase)
inverso=[]
for c in range (caracteres-1,-1,-1):
    inverso.append(frase[c])
    #print(inverso)
    compara=''.join(inverso)
    compara=compara.lower()

if frase==compara:
    print(f'Sim, a frase "{x}" é um palíndromo')
else:
    print(f'Não, a frase "{x}" não é um palíndromo')