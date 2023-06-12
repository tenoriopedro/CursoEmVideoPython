from datetime import date
ano_atual = date.today().year
cont = 0
contm = 0
for c in range(1, 8):
    ano_nascimento = int(input(f'Qual o ano da {c}º pessoa: '))
    maioridade = ano_atual - ano_nascimento
    menoridade = ano_atual - ano_nascimento
    if maioridade >= 21:
        cont += 1
    elif menoridade < 21:
        contm += 1
print('Considerando que a maior idade é de 21 anos em diante..')
print(f'Neste grupo há {cont} pessoas maiores de idade.')
print(f'E também há {contm} pessoas menores de idade')

