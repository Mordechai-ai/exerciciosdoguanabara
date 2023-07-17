numero=int(input('Digite um número de 0 a 9999:'))
milhares=(numero//1000)
numerocent=(numero%1000)
centenas=(numerocent//100)
numerodez=(numerocent%100)
dezenas=(numerodez//10)
unidades=(numerodez%10)
print(f'Milhares: {milhares}')
print(f'Centenas: {centenas}')
print(f'dezenas: {dezenas}')
print(f'Unidades: {unidades}')


