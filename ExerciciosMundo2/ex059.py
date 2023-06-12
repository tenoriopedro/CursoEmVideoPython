n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print('Agora..')
multiplicar = 0
soma = 0
fim = False
while not fim:
    print('''
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos numeros
[ 5 ] para sair do progama
''')
    escolha = int(input('Escolha o que quer fazer: '))
    if escolha == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} = {soma}')
        print('=-' *20)
    if escolha == 2:
        multiplicar = n1 * n2
        print(f'O resultado de {n1} x {n2} = {multiplicar}')
        print('=-' * 20)
    if escolha == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        elif n2 > n1:
            print(f'{n2} é maior que {n1}')
        else:
            print('Não tem numero maior pois os numeros são iguais')
        print('=-' * 20)
    if escolha == 4:
        n3 = int(input('Digite outro numero: '))
        n4 = int(input('Digite outro numero: '))
        n1 = n3
        n2 = n4
        print('=-' * 20)
    if escolha > 5:
        print('Opção invalida, tente novamente.')
        print('=-' * 20)
    else:
        if escolha == 5:
            fim = True
print('--VOCÊ SAIU DO PROGRAMA--')


                # OUTRA MANEIRA:
#opção = 0
#while opção != 5:
#    opção = int(input('Qual sua opção?'))