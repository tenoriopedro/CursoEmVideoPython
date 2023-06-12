numero1 = float(input('Digite seu primeiro numero: '))
numero2 = float(input('Digite seu segundo numero: '))
if numero1 > numero2:
    print('O primeiro valor é o maior')
elif numero2 > numero1:
    print('O segundo valor é o maior')
elif numero1 == numero2:
    print('Não existe valor maior pois os dois são iguais')