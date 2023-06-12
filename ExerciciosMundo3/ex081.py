numero = []


while True:
    n = int(input('Digite um valor: '))
    numero.append(n)
    pergunta = ' '
    while pergunta not in 'sn':
        pergunta = str(input('Quer continuar [S/N]: ')).strip().lower()[0]
    if pergunta == 'n':
        break
print('=' *40)
print(f'Esta lista tem {len(numero)} elementos.')
numero.sort(reverse=True)
print(f'Valores em ordem decrescente: {numero}')

if 5 in numero:
    print(f'O valor 5 FAZ parte da lista ')
else:
    print('O valor 5 NÃO FAZ parte da lista')
