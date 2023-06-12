print('-=' *10)
print('CALCULANDO FATORIAL')
print('-=' *10)
n = int(input('Escolha um número para o calculo do fatorial: '))
count = 1
resultado = 1
while count <= n:
    resultado *= count
    count += 1
print(f'{n}! = {resultado}')

                    #OUTRA MANEIRA
#n = int(input('Digite um numero para calcular seu fatorial: '))
#c = n
#f = 1
#print(f'Calculando {n}! = ', end='')
#while c > 0:
#    print(f'{c}', end='')
#    print(' x ' if c > 1 else ' = ', end='')
#    f *= c
#    c -= 1
#print(f'{f}.')
                    #COM "FOR"
#n = int(input('Digite um numero: '))
#c = n
#f = 1
#print(f'Calculando {n}! = ', end='')
#for c in range(n, 0, -1):
#    print(f'{c}', end='')
#    print(' x ' if c > 1 else ' = ', end='')
#    f *= c
#    c -= 1
#print(f'{f}')