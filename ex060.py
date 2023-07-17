print("CALCULE O FATORIAL\n")

x = int(input("Digite o número fatorial a ser calculado: "))

n = 1
fat = 1
while n <= x:
    fat = fat * n
    n = n + 1

print(f"{x}! é igual a {fat}")
