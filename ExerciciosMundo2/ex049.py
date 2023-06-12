print('HORA DA TABUADA')
num = int(input('Escolha um numero, para começarmos a tabuada: '))
for c in range(0, 11):
    mult = num * c
    print('{} x  {} = {}'. format(num, c, mult))