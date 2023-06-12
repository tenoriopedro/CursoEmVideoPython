h = float(input('Qual a altura da sua parede? '))
l = float(input('E qual a largura? '))
a = h * l
print('A area da sua parede é de {:.2f}m2'.format(a))
t = a / 2
print('E para pintar será necessário {:.2f}l de tinta'.format(t))
