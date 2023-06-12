print('*' *20)
print('   NÚMEROS PRIMOS')
print('*' *20)
numero = int(input('Digite um número: '))
multiplo = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        multiplo += 1
    print('{} '.format(c), end='')
print(f'\nO numero {numero} foi divisivel {multiplo} vezes.')
if multiplo == 2:
    print(f'O numero {numero} é primo')
else:
    print(f'O numero {numero} não é primo')


