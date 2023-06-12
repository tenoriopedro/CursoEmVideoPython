from time import sleep
soma = 0
cont = 0
conti = 0
for num in range(0, 6):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        cont += 1
        soma += num
    elif num % 2 == 1:
        conti += 1
print('São {} numeros pares'.format(cont))
print('E a soma desses numeros pares são {}'.format(soma))
print('E também são {} numeros impares, porem serão desconsiderados'.format(conti))
sleep(2)
wait = input('Pressiona ENTER pra TERMINAR')
print('--FIM--')
