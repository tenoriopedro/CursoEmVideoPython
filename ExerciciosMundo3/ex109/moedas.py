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
