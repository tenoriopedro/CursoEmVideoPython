while True:
    numero = int(input('Quer ver a tabuada de qual valor: '))
    print('_' *40)
    if numero < 0:
        break
    for c in range(0 ,11):
        produto = numero * c
        print(f'{numero} x {c} = {produto}')
    print('_' *40)
print('PROGRAMA ENCERRADO. Volte sempre!')