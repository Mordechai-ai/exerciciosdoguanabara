p1=float(input('Prova1: '))
p2=float(input('Prova2: '))
media=((p1+p2)/2)
print(media)
if media<6:
    print(f'Sua média é {media}, vc está REPROVADO')
elif media>6 and media<7:
    print(f'Sua média é {media}, vc está de RECUPERAÇÃO')
elif media >=7:
    print(f'Sua média é {media}, vc está APROVADO')
