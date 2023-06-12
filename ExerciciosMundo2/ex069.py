cont_idade = 0
cont_man = 0
cont_menina = 0
while True:
    print('CADASTRE UMA PESSOA')
    print('*' *20)
    idade = int(input('Qual idade: '))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Sexo [M/F]: ')).strip().lower()[0]
    print('*' *20)
    pergunta = ' '
    while pergunta not in 'SsNn':
        pergunta = str(input('Quer continuar [S/N]: ')).strip().lower()[0]
    print('*' *20)
    if idade >= 18:
        cont_idade += 1
    if sexo in 'm':
        cont_man += 1
    if sexo in 'f' and idade < 20:
        cont_menina += 1
    if pergunta in 'n':
        break
print('NESTE GRUPO..')
print(f'Tem {cont_idade} pessoas maiores de 18 anos')
print(f'Tem {cont_man} homens cadastrados')
print(f'Tem {cont_menina} mulheres abaixo dos 20 anos')