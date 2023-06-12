km = float(input('Qual a distancia, em kms, da sua viagem? '))
if km > 200:
    print('A sua passagem custará {:.2f}'.format(km * 0.45))
else:
    print('A sua passagem custará {:.2f}'.format(km * 0.50))
print('Faça uma boa viagem')
