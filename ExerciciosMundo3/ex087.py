matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para posição {linha}, {coluna}: '))
print('-=' *30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print('-=' *30)
for numeros in range(0, len(matriz)):
    for numero in matriz[numeros]:
        if numero % 2 == 0:
            soma += numero
print(f'A soma de todos os valores pares dá {soma}.')
soma_coluna = matriz[0][2] + matriz[1][2] + matriz[2][2]
#for linha in range(0, 3):
#    soma_coluna += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é {soma_coluna}')
valor_maior = 0
for valor in matriz[1]:
    if valor == matriz[1]:
        valor_maior = valor
    elif valor > valor_maior:
            valor_maior = valor
print(f'O maior valor da segunda coluna é {valor_maior}')