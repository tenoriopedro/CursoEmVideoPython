from random import randint

def sortear(lista):
    print(f'Os 5 numeros sorteados são:', end=' ')
    for c in range(0, 5):
        c = randint(0, 10)
        print(f'{c} ', end='')
        lista.append(c)

def somaPar(lista):
    print(f'\nSomando os valores pares dos números sorteados temos: ', end='')
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(soma)

numero = []
sortear(numero)
somaPar(numero)