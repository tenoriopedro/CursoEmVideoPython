 #Programa para comprar uma casa
#Perguntar valor da casa, salario e quantos anos vai pagar
#Calcular valor da prestação mensal
#Sabendo que não pode exceder 30% do salario
# ou entao sera negado
print('='* 20)
print('APROVAÇÃO DE CRÉDITO')
print('='* 20)
nome_vendedor = str(input('Nome do vendedor: '))
c = float(input('Qual valor da casa, {}? '.format(nome_vendedor)))
s = float(input('Qual salário do comprador, {}? €'.format(nome_vendedor)))
a = int(input('Em quantos anos o comprador quer pagar, {}? '.format(nome_vendedor)))
print(' ')
print('{}, de acordo com as regras da empresa...'.format(nome_vendedor))
print(' ')
pm = c /(12 * a)
exs = s * 0.30
if exs <= pm:
    print('O credito para o seu comprador \033[1;31mNÃO FOI APROVADO\033[m')
    print('Pois a \033[4mtaxa de esforço\033[m do comprador que é de {:.2f}€'.format(exs))
    print('Não coincide com o valor necessario')
else:
    print('O credito para seu comprador foi \033[1;32mAPROVADO\033[m')
    print('Pois a \033[4mtaxa de esforço\033[m do comprador que é de {:.2f}€'.format(exs))
    print('Coincide com as regras da empresa')
print(' ')
print('Obrigado {} e tenha um otimo dia!'.format(nome_vendedor))
