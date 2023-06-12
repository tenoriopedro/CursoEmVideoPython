def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um numero
    :param n: Numero que sera calculado
    :param show:(opcional) mostrara o calculo
    :return: o resultado do fatorial de n
    """
    f = 1
    while n > 0:
        if show:
            print(f'{n}', end='')
            print(' x ' if n > 1 else ' = ', end='')
        f *= n
        n -= 1
    return f'{f}'
resposta = int(input('Deseja fazer o fatorial de qual numero: '))
mostrar = str(input('Quer ver o calculo[S/N]: ')).strip().lower()[0]
if mostrar in 's':
    print(fatorial(resposta, show=True))
elif mostrar in 'n':
    print(fatorial(resposta, show=False))