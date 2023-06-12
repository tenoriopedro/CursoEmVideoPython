def titulo(msg):
    from time import sleep
    sleep(1)
    print('~' *40)
    print(f'{msg}'.center(40))
    print('~' *40)
    print('''1 - Ver pessoas cadastradas
2 - Cadastrar nova pessoa 
3 - Sair do sistema''')
    print('~' * 40)

def leiaOpcao(msg):
    while True:
        try:
            opçao = int(input(msg))
            if opçao == 1:
                print('~' *40)
                print('VER PESSOAS CADASTRADAS'.center(40))
                print('~' *40)
                return 1
                break
            if opçao == 2:
                print('~' * 40)
                print('CADASTRAR NOVAS PESSOAS'.center(40))
                print('~' * 40)
                return 2
                break
            if opçao == 3:
                print('~' * 40)
                print('Saindo do sistema... Até logo.'.center(40))
                print('~' * 40)
                return 3
                break
            else:
                print(f'\033[31mERRO!! Por favor, digite as opções de 1 a 3.\033[m')
        except (ValueError, TypeError):
            print(f'\033[31mERRO!! Por favor, digite as opções de 1 a 3.\033[m')
            continue

