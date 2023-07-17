valor=float(input('Valor do imóvel : R$ '))
salario=float(input('Salário Mensal: R$ '))
anos=int(input('Prazo de Pagamento em Anos: '))
meses=(anos*12)
parcelareal=(valor/meses)
parcpossivel=(0.3*salario)
if parcelareal>parcpossivel:
    print(f'O valor da parcela, de R$ {parcelareal:.2f} ultrapassa o valor de R$ {parcpossivel:.2f} \n que representa 30% do seu salário')
    print(f'Empréstimo negado')
else:
    print(f'O valor da parcela, de R$ {parcelareal:.2f} está de acordo com os seus ganhos')


