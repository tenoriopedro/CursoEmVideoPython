d = int(input('O carro foi usado por quantos dias? '))
k = float(input('O carro percorreu quantos kms? '))
x = (d * 60) + (k * 0.15)
print('O aluguel do carro fica por {:.2f}R$'.format(x))
