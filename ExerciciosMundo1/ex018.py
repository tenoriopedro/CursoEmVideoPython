import math
num = float(input('Digite um angulo: '))
co = math.cos(math.radians(num))
s = math.sin(math.radians(num))
t = math.tan(math.radians(num))
print('O valor do cosseno é {:.2f}\nO valor do seno é {:.2f}\nO valor da tangente é {:.2f}.'.format(co, s, t))

