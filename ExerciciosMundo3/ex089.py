notas_alunos = []
boletim = []

while True:
    nome_aluno = str(input('Qual nome do aluno: ')).strip()
    notas_alunos.append(nome_aluno)

    nota1 = float(input('Primeira nota: '))
    notas_alunos.append(nota1)

    nota2 = float(input('Segunda nota: '))
    notas_alunos.append(nota2)

    #media = (nota1 + nota2) / 2
    #medias.append(media)

    boletim.append(notas_alunos[:])
    notas_alunos.clear()

    pergunta = ' '
    while pergunta not in 'sn':
        pergunta = str(input('Quer continuar [S/N]? R: ')).lower().strip()[0]
    if pergunta == 'n':
        break
print('=-' *40)

print(f'{"Nº":<4}{"NOME":<10}{"MEDIA":>8}    {"SITUAÇÃO":>10}')
for j, p in enumerate(boletim):
    media = (p[1] + p[2]) / 2
    print(f'{j+1:<4}{p[0]:<10}{media:>8.1f}', end='    ')
    if media > 7.0:
        print(f'{"APROVADO":>10}')
    else:
        print(f'{"REPROVADO":>11}')

while True:
    print('=-' *40)
    resposta = 0
    while resposta <= len(boletim):
        resposta = int(input('Mostrar notas de qual aluno? (999 para interromper) R: '))
        if resposta > len(boletim) and resposta != 999 or resposta < 1:
            print('ERRO NA RESPOSTA, tente novamente...')
        elif resposta <= len(boletim) and resposta != 999:
            print(f'As notas do Aluno {boletim[resposta-1][0]} são: {boletim[resposta-1][1:]}')
            print('-=' *40)
    if resposta == 999:
        print('FINALIZANDO...')
        break

print('=-' *40)
print('PROGRAMA FINALIZADO, VOLTE SEMPRE!!!')