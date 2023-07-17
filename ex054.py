import datetime
anoatual=datetime.date.today().year


maiores=0
menores=0

for c in range (1,8,1):
    anoborn=int(input('Digite o seu ano de nascimento: '))
    if anoatual-anoborn>=18:
        maiores=maiores+1
    else:
        menores=menores+1
print(f'\nHoje em {anoatual}, {menores} pessoas ainda não atingiram a maioridade')
print(f'\nHoje em {anoatual}, {maiores} pessoas já são maiores')
