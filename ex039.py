import datetime
anonasc=int(input(f'Digite o ano de nascimento: '))
mesnasc=int(input(f'Digite o mês de nascimento: '))
dianasc=int(input(f'Digite o dia de nascimento: '))
dataatual=datetime.date.today()
print(f'Hoje é {dataatual}')
datanasc=datetime.date(anonasc,mesnasc,dianasc)
print(f'Sua Data de Nascimento é {datanasc}')
diferençadias=dataatual-datanasc
#print(diferençadias)
datazero=(dataatual-datetime.timedelta(days=365*18))
print(f'Pessoas nascidas antes de {datazero} precisam se alistar')
difdatazero=(datazero-datanasc).days
difmeses=(difdatazero//30)
#print(f'Target para alistamento:  {difmeses}')
if datanasc>datazero:
    print(f'Vc ainda vai se alistar.Faltam aproximadamente {-difmeses} meses')
else:
    print(f'Vc está atrasado aproximadamente {difmeses} meses com seu alistamento militar.')
