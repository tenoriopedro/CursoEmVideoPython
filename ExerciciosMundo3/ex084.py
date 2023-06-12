pessoas_dados = []
todos = []
menor_peso = maior_peso = totpessoas = 0
while True:
    pessoas_dados.append(str(input('Nome: ')))
    pessoas_dados.append(float(input('Peso: ')))
    if len(todos) == 0:
        maior_peso = menor_peso = pessoas_dados[1]
    else:
        if pessoas_dados[1] > maior_peso:
            maior_peso = pessoas_dados[1]
        if pessoas_dados[1] < menor_peso:
            menor_peso = pessoas_dados[1]
    todos.append(pessoas_dados[:])
    pessoas_dados.clear()
    pergunta = ' '
    while pergunta not in 'sn':
        pergunta = str(input('Quer continuar [S/N]: ')).strip().lower()[0]
    if pergunta == 'n':
        break
for dados in todos:
    if dados[0]:
        totpessoas += 1
print('-=' *30)
print(f'Foram cadastradas {totpessoas} pessoas')
print(f'O maior peso foi {maior_peso}Kg. E o peso foi', end=' ')
for dados in todos:
    if dados[1] == maior_peso:
        print(f'"{dados[0]}"', end=' ')
print(f'\nO menor peso foi {menor_peso}Kg. E o peso foi', end=' ')
for dados in todos:
    if dados[1] == menor_peso:
        print(f'"{dados[0]}"', end=' ')
