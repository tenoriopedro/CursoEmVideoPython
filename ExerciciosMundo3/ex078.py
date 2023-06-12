valores = []
maior = 0
menor = 0
for pos in range(0, 5):
    valores.append(int(input(f'Digite um valor para a {pos +1}ª posição : ')))
    if pos == 0:
        maior = valores[pos]
        menor = valores[pos]
    else:
        if valores[pos] < menor:
            menor = valores[pos]
        if valores[pos] > maior:
            maior = valores[pos]
print('-=' *40)
print(f'Você digitou os valores {valores}.')
print(f'O maior valor digitado foi {maior} nas posições ',end=' ')
for posiçãomaior, valor in enumerate(valores):
    if valor == maior:
        print(f'{posiçãomaior}...', end=' ')
print(f'\nO menor valor digitado foi {menor} nas posições ', end=' ')
for posiçãomenor, valor in enumerate(valores):
    if valor == menor:
        print(f'{posiçãomenor}...',end=' ')
