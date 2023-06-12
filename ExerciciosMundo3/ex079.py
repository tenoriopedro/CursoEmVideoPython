numeros = []

while True:
    n = int(input('Digite um número: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valor não adicionado')
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if resposta == 'N':
        break
numeros.sort()
print(f'A lista que você digitou em ordem crescente: {numeros}')
