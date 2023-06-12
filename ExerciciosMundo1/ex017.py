from math import pow, sqrt
co = float(input('Qual comprimento do cateto oposto? '))
ca = float(input('Qual comprimento do cateto adjacente? '))
s = pow(ca, 2) + pow(co, 2)
print('A hipotenusa desse triangulo é {:.2f}'.format(sqrt(s)))
