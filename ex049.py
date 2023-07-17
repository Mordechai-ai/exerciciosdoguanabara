numero=int(input('Qual tabuada você quer? '))
print(f'\033[4:31mTABUADA DO {numero}\033[m')
for c in range (1,11):
    print(f'{numero} x {c} = {numero*c} ')