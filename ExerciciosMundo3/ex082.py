todos_numeros = []
numeros_pares = []
numeros_impares = []

while True:
    n = int(input('Digite um valor: '))
    todos_numeros.append(n)
    pergunta = ' '
    while pergunta not in 'sn':
        pergunta = str(input('Quer continuar [S/N]: ')).strip().lower()[0]
    if pergunta == 'n':
        break
for c in todos_numeros:
    if c % 2 == 0:
        numeros_pares.append(c)
    else:
        numeros_impares.append(c)
todos_numeros.sort()
numeros_pares.sort()
numeros_impares.sort()
print(f'A lista completa: {todos_numeros}')
print(f'A lista de pares é: {numeros_pares}')
print(f'A lista de impares é: {numeros_impares}')