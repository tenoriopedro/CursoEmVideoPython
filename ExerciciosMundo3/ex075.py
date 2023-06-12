n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um numero: '))
n4 = int(input('Digite um numero: '))
numeros = (n1, n2, n3, n4)
print(f'Os numeros digitados foram: {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 está na {numeros.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado')
print(f'O numero par digitado foi ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')

#### OUTRA MANEIRA MAIS FACIL:
#numeros = ( int(input('Digite um numero: ')),
#            int(input('Digite um numero: ')),
 #           int(input('Digite um numero: ')),
  #          int(input('Digite um numero: ')))
