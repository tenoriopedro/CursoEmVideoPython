somaidade = 0
maior = 0
nomevelho = ''
mulher = 0
contmulher = 0
for p in range(1, 5):
    print(f'{p}º PESSOA')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip()
    somaidade += idade
    media = somaidade / 4
    if p == 1 and sexo in 'Mm':
        maior = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maior:
        maior = idade
        nomevelho = nome
    if idade < 20 and sexo in 'Ff':
        contmulher += 1
print(f'A média de idade do grupo é de {media:.2f} anos')
print(f'O homem mais velho tem {maior} anos e se chama {nomevelho}')
print(f'E tem {contmulher} mulheres abaixo dos 20 anos')
