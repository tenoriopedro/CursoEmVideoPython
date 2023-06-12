print('=' *20)
print('  \033[1mCALCULADORA IMC\033[m')
print('=' *20)
altura = float(input('Digite aqui sua altura: '))
peso = float(input('Digite aqui seu peso: '))
resultado = peso / (altura * altura)
if resultado < 18.5:
    print('O seu IMC é de {:.1f} .'.format(resultado))
    print('De acordo com esses números você está ABAIXO DO PESO.')
elif resultado <= 25:
    print('O seu IMC é de {:.1f} .'.format(resultado))
    print('De acordo com esses números você está no PESO IDEAL.')
elif resultado <= 30:
    print('O seu IMC é de {:.1f} .'.format(resultado))
    print('De acordo com esses números você está com SOBREPESO.')
elif resultado <= 40:
    print('O seu IMC é de {:.1f} .'.format(resultado))
    print('De acordo com esses números você está com OBESIDADE.')
else:
    print('O seu IMC é de {:.1f} .'.format(resultado))
    print('De acordo com esses números você está com OBESIDADE MÓRBIDA')