# ***COISA NOVA
# != - diferente
# and // or
#Plus! Para analisar o ano atual \/
#import datatime OU from datatime import data
# ano atual = date.today().year

from datetime import date
print('-=-=' * 10)
print('Quer saber se um ano é bissexto?')
print('-=-=' * 10)
ano = int(input('Digite o ano aqui (para ano atual digite 0): '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é um ano bissexto'.format(ano))
else:
    print('O ano {} não é um ano bissexto'.format(ano))
