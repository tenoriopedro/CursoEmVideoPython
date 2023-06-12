#from random import sample
#sorteados = sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 0] , k=5)
#print(f'Os numeros sorteados são: {sorteados}')
#print(f'O maior número é o {max(sorteados)}')
#print(f'E o menor número é o {min(sorteados)}')

#  OUTRA MANEIRA:
from random import randint
numeros = (randint(0, 10), randint(0, 10),randint(0, 10),
           randint(0, 10), randint(0, 10))
print('Os valores sorteados são: ',end='')
for n in numeros:
    print(f'{n} ', end='')