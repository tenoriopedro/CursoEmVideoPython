def aumentar(n=0, t=0):
    v = n * (1 + t / 100)
    return v

def diminuir(n=0, t=0):
    v = n * (1 - t / 100)
    return v

def dobro(n=0):
    return n * 2

def metade(n=0):
    if formt:
        return '€'
    return n / 2

def moeda(n=0):
    return f'€{n:.2f}'.replace('.', ',')
