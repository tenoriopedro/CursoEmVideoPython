print('Calculando notas ')
b1 = float(input('b1: '))
b2 = float(input('b2: '))
b3 = float(input('b3: '))
b4 = float(input('b4: '))
media = (b1 + b2 + b3 + b4) / 4
if media < 5.0:
    print('A média do aluno é {:.1f} \nInfelizmente aluno está REPROVADO'.format(media))
elif media >= 7.0:
    print('A media do aluno é de {:.1f} \nO aluno está APROVADO.'.format(media))
elif media >= 5.0 and media < 7:
    print('A média do aluno é de {:.1f} \nO aluno esta em RECUPERAÇÃO'.format(media))