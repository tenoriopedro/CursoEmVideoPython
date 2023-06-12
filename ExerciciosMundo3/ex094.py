cadastro = []
cont = 0
tot_idade = 0
pessoas = {}
while True:
    pessoas['nome'] = str(input('Nome: ')).strip().title()
    pessoas['sexo'] = ' '
    while pessoas['sexo'] not in 'MF':
        pessoas['sexo'] = str(input('Sexo[M/F]: ')).upper().strip()[0]
        if pessoas['sexo'] not in 'MF':
            print('ERRO!! Por favor apenas M ou F.')
    check = True
    while check == True:
        pessoas['idade'] = input('Idade: ')
        if pessoas['idade'].isnumeric() == True:
            check = False
        else:
            check = True
            print('ERRO!! Por favor, digite apenas números.')
    pessoas['idade'] = int(pessoas['idade'])
    tot_idade += pessoas['idade']
    cadastro.append(pessoas.copy())
    pergunta = ' '
    while pergunta not in 'sn':
        pergunta = str(input('Deseja continuar[S/N]: ')).lower().strip()[0]
        if pergunta not in 'sn':
            print('ERRO!! Apenas responda S ou N.')
    if pergunta == 'n':
        break
print('-=' *30)
print(f' -> Foram ao todo {len(cadastro)} pessoas cadastradas.')

media = tot_idade / len(cadastro)
print(f' -> A média de idade do grupo cadastrado é de {media:.2f} anos')

print(' -> As mulheres cadastradas:', end=' ')
for p in cadastro:
    if p['sexo'] in 'Ff':
        print(p['nome'], end=' ')
print()
print(f' -> Lista das pessoas com a idade acima da média: ')
for item in cadastro:
    if item['idade'] > media:
        for k, v in item.items():
            print(f'    {k} = {v}; ', end='')
        print()