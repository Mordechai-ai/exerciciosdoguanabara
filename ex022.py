nome=str(input('Digite seu nome completo:'))
print(nome.upper())
print(nome.lower())
soletras=(nome.replace(' ',''))
numero=(len(soletras))
print(f'Seu nome completo tem {numero} letras')
nomes=(nome.split())
print(f'Seu primeiro nome é {nomes[0]}')
print(f'Seu primeiro nome tem {len(nomes[0])} letras')


