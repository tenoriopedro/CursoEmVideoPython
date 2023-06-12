# Multa 7€ por cada km acima do limite
v = float(input('Qual a velocidade do carro? '))
if v > 80:
    print('VOCÊ FOI MULTADO!!!! E sua multa será de {:.2f}€'.format((v - 80) * 7))
