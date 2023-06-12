def leiaInt(n):
    while True:
        num = input(n)
        if num.isnumeric():
            num = int(num)
            return num
            break
        else:
            print('\033[31mERRO!! Digite um numero inteiro valido\033[m')


n = leiaInt('Digite um numero: ')
print(f'Você acabou de digitar o numero {n}')