'''Ler ano de nascimento e informar se ainda vai se alistar
se esta na hora, ou se ja passou da hora'''

from datetime import date
print('='* 20)
print('\033[1;32mALISTE-SE JÁ\033[m')
print('='* 20)
sexo = str(input('Qual seu sexo, masculino ou feminino: '))
if sexo == 'feminino':
    print('Seu alistamento não é obrigatório, caso queira continuar informe seu ano.')
nascimento = int(input('Digite aqui seu ano de nascimento: '))
ano_atual = date.today().year
alistar = ano_atual - nascimento
diferença = alistar - 18
if alistar < 18:
    print('Você tem {} anos e ainda não esta na hora de se alistar.'.format(alistar))
    print('Faltam {} ano(s) para você se alistar.'.format(- diferença))
    print('O seu alistamento será em {}.'.format(ano_atual - diferença))
elif alistar > 18:
    print('Você tem {} anos e já passou da hora se alistar.'.format(alistar))
    print('Você esta atrasado {} anos, se ainda não o fez, vá fazer!!!!'.format(diferença))
    print('Seu alistamento foi em {}.'.format(ano_atual - diferença))
elif alistar == 18:
    print('Você tem {} anos e esta na idade certa!'.format(alistar))
    print('Vá se alistar!!!!')
