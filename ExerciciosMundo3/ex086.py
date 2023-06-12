###OUTRA MANEIRA###
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para posição {linha}, {coluna}: '))
print('=-' *30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end=' ')
    print()
#matriz = [[], [], []]
#for n in range(0, 3):
#    valor = int(input(f'Digite o valor para posição [0, {n}]: '))
#    matriz[0].append(valor)
#for n in range(0, 3):
#    valor = int(input(f'Digite o valor para posição [1, {n}]: '))
#    matriz[1].append(valor)
#for n in range(0, 3):
#    valor = int(input(f'Digite o valor para posição [2, {n}]: '))
#    matriz[2].append(valor)


#print(f'''
#  [ {matriz[0][0]} ]  [ {matriz[0][1]} ]  [ {matriz[0][2]} ]
#  [ {matriz[1][0]} ]  [ {matriz[1][1]} ]  [ {matriz[1][2]} ]
#  [ {matriz[2][0]} ]  [ {matriz[2][1]} ]  [ {matriz[2][2]} ]''')