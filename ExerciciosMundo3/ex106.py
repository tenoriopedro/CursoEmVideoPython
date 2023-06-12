from time import sleep
cor = ['\033[m',          # 0 nenhuma
       '\033[0;30;41m',   # 1 vermelha
       '\033[0;30;42m',   # 2 verde
       '\033[0;30;43m',   # 3 amarelo
       '\033[0;30;44m',   # 4 azul
       ]


def ajuda(n):
    print(cor[4], end='')
    help(n)
    print(cor[0],end='')

def tit(msg, c=0):
    tam = len(msg) + 4
    print(cor[c], end='')
    print('~' *tam)
    print(f'  {msg}')
    print('~' *tam)
    print(cor[0], end='')


comando = ''
while True:
    tit('SISTEMA DE AJUDA PYTHON', 2)
    print(cor[3], end='')
    comando = str(input('Digite a Função: '))
    print(cor[0], end='')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

tit('OBRIGADO POR USAR O NOSSO SISTEMA DE AJUDA PYTHON', 4)

