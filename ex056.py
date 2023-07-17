x=0
somaidade=0
listanomes=[]
listaidades=[]
listasexo=[]
mulheresmenos20=0

for c in range (1,5):
    nome=str(input('\nNome: '))
    idade=int(input('Idade: '))
    sexo=str(input('Sexo(M/F): '))
    sexo=sexo.upper()
    listanomes.append(nome)
    listaidades.append(idade)
    listasexo.append(sexo)
    somaidade=somaidade+idade
    x=x+1
    if sexo=='F' and idade<20:
        mulheresmenos20=mulheresmenos20+1

media=somaidade/x
print(f'A média da idade das pessoas é {media:.0f}')
locmaior=listaidades.index(max(listaidades))

if listasexo[locmaior]=='M':
    print(f'O homem mais velho se chama {listanomes[locmaior]} e ele tem {listaidades[locmaior]} anos')

print(f'O número de mulheres com menos de 20 anos é {mulheresmenos20}')
