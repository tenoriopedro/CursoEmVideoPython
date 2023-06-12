def aumentar(n=0, t=0, formt=False):
    v = n * (1 + t / 100)
    if formt:
        return f'€{v:.2f}'.replace('.', ',')
    else:
        return v

def diminuir(n=0, t=0, formt=False):
    v = n * (1 - t / 100)
    if formt:
        return f'€{v:.2f}'.replace('.', ',')
    else:
        return v

def dobro(n=0, formt=False):
    v = n * 2
    if formt:
        return f'€{v:.2f}'.replace('.',',')
    else:
        return v

def metade(n=0, formt=False):
    if formt:
        return f'€{n / 2:.2f}'.replace('.', ',')
    else:
        return n / 2
def moeda(n=0):
    return f'€{n:.2f}'.replace('.', ',')


def resumo(n=0, aumento=0, diminui=0):
    print('~' *30)
    print('RESUMO DO VALOR'.center(30))
    print('~' *30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metado do preço: \t{metade(n, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(n, aumento, True)}')
    print(f'{diminui}% de redução: \t{diminuir(n, diminui, True)}')
    print(f'~' *30)