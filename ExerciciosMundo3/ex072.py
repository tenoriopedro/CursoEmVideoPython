numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
opçao = ' '
while True:
    numero = int(input('Digite um numero entre 0 e 20: '))
    if numero > 20 or numero < 0:
        print('TENTE NOVAMENTE')
    if numero >= 0 and numero <= 20:
        print(f'Você digitou o numero {numeros[numero]}')
        opçao = str(input('Quer continuar [S/N]: ')).strip().lower()[0]
        if opçao == 'n':
            break
print('FIM DO PROGRAMA')