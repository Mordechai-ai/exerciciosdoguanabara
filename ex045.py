#1 PEDRA
#2 PAPEL
#3 TESOURA
pc=0
pv=0
print('\033[31mJOKENPÔ! PEDRA PAPEL TESOURA!\033[m')
rodadas=int(input('Quantas rodadas você quer jogar?: '))
for c in range (1,rodadas):

  import random
  #compu=1
  compu=random.randint(1,3)
  #print(compu)
  escolha=int(input('Escolha:\n  (1)PEDRA\n  (2)PAPEL\n  (3)TESOURA\n  Digite o número: '))

#VER
  lista=[escolha,compu]
  #print(lista)

  if lista[0]==1 and lista[1]==2:
    print(f'Você:Pedra\nComputador:Papel\nPERDEU!\n\n')
    pc=pc+1

  elif lista[0]==2 and lista[1]==1:
    print(f'\n\nVocê:Papel\nComputador:Pedra\nGANHOU!\n\n')
    pv=pv+1

  elif lista[0]==1 and lista[1]==3:
    print(f'\n\nVocê:Pedra\nComputador:Tesoura\nGANHOU!\n\n')
    pv=pv+1

  elif lista[0]==3 and lista[1]==1:
    print(f'\n\nVocê:Tesoura\nComputador:Pedra\nPERDEU!\n\n')
    pc=pc+1

  elif lista[0]==2 and lista[1]==3:
    print(f'\n\nVocê:Papel\nComputador:Tesoura\nPERDEU!\n\n')
    pc=pc+1

  elif lista[0]==3 and lista[1]==2:
    print(f'\n\nVocê:Tesoura\nComputador:Papel\nGANHOU!\n\n')
    pv=pv+1

  elif lista[0]==lista[1]:
      print(f'\n\nAmbos escolheram {lista[0]}\nEMPATOU!\n\n')

print('\033[4:31mRESULTADO\033[m')
print(f'Você: {pv}')
print(f'Computador:{pc}')