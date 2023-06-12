print('='* 30)
print('\033[34mCONVERSOR DE NÚMEROS\033[m')
print('\033[34mBINÁRIOS, HEXADECIMAL OU OCTAL\033[m')
print('='* 30)
print('')
numero = int(input('Digite seu numero aqui: '))
print('Agora escolha UMA das TRÊS opções')
print('[ 1 ] para binário \n[ 2 ] para hexadecimal \n[ 3 ] para octal')
escolha = int(input('Escolha o numero do seu conversor: '))
if escolha == 1:
    print('Para binário o nº será: {}'.format(bin(numero) [2:]))
elif escolha == 2:
    print('Para hexadecimal o nº será: {}'.format(hex(numero) [2:]))
elif escolha == 3:
    print('Para octal o nº será: {}'.format(oct(numero) [2:]))
else:
    print('Opção INVALIDA, tente novamente')