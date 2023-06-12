from datetime import date
print('='* 30)
print('\033[1;34mCONFEDERAÇÃO NACIONAL DE NATAÇÃO\033[m')
print('='* 30)
ano_atual = date.today().year
ano_atleta = int(input('Qual o ano de nascimento do atleta: '))
idade = ano_atual - ano_atleta
print('')
if idade <= 9:
    print('O atleta tem {} anos.'.format(idade))
    print('Portanto o atleta faz parte da categoria MIRIM.')
elif idade <= 14 and idade > 9:
    print('O atleta tem {} anos.'.format(idade))
    print('Portanto o atleta faz parte da categoria INFANTIL.')
elif idade > 14 and idade <= 19:
    print('O atleta tem {} anos.'.format(idade))
    print('Portanto o atleta faz parte da categoria JUNIOR.')
elif idade > 19 and idade <= 25:
    print('O atleta tem {} anos.'.format(idade))
    print('Portanto o atleta faz parte da categoria SÊNIOR.')
elif idade > 25:
    print('O atleta tem {} anos.'.format(idade))
    print('Portanto o atleta faz parte da categoria MASTER.')
