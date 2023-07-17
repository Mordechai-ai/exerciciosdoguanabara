lista=[]
for c in range (1,6):
    peso=float(input('Qual o seu peso(Kg)? '))
    lista.append(peso)
maior=max(lista)
menor=min(lista)
print(f'\nO maior peso foi {maior} Kg')
print(f'O menor peso foi {menor} Kg')
