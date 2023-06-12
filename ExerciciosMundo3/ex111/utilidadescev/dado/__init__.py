def leiaDinheiro(msg):
    """
    -> Função que valida a entrada de um preço(numero float)
    :param msg: recebe o preço
    :return: retorna o numero(preço) validado
    """
    while True:
        num = input(msg).strip().replace(',', '.')
        if num.isnumeric():
            num = float(num)
            return num
            break
        if '.' in num:
            num = float(num)
            return num
            break
        else:
            print(f'\033[31mERRO!! "{num}" é um preço inválido.\033[m')


def leiaInt(n):
    """
    -> Função que valida se é um numeiro inteiro
    :param n: recebe o numero
    :return: retorna o numero inteiro válido
    """
    while True:
        try:
            num = int(input(n))
        except (ValueError, TypeError):
            print('\033[31mERRO!! Digite um numero inteiro valido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[33mPrograma interrompido pelo usuário.\033[m')
            return 0
        else:
            return num


def leiaFloat(n):
    """
    -> Função que vai validar se é um numero real
    :param n: recebe o numero
    :return: retorna o numero real valido
    """

    while True:
        try:
            num = input(n).replace(',', '.')
            num = float(num)
        except (ValueError, TypeError):
            print('\033[31mERRO!! Por favor digite um numero real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[33mPrograma interrompido pelo usuário.\033[m')
            return 0
        else:
            return num
