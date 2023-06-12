print('PROGRESSÃO ARITMETICA')
print('-=' *10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
count = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while count <= total:
        print(f'{termo}', end= ' -> ')
        termo += razao
        count += 1
    print('PAUSA')
    mais = int(input('Deseja mostrar mais quantos termos? '))
print(f'Você terminou a sessão com {total} termos mostrados')

