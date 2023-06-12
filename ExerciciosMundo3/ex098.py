from time import sleep

def linha():
    print('~' *30)


def escreva(msg):
    print('~' *(len(msg) + 4))
    print(f'  {msg}')
    print('~'*(len(msg) + 4))
    sleep(2.0)

def contador(x, y, z):
    if z < 0:
        z *= -1
    sleep(1)
    print(f'Contagem de {x} até {y}, de {z} em {z}:')
    sleep(0.5)
    if x > y:
        print('- ORDEM DECRESCENTE -')
        sleep(2.5)
        cont = x
        while cont >= y:
            print(f'{cont} ',end='')
            sleep(0.5)
            cont -= z
    else:
        print('- ORDEM CRESCENTE -')
        sleep(2.5)
        cont = x
        while cont <= y:
            print(f'{cont} ',end='' )
            sleep(0.5)
            cont += z
    print('-> FIM')
    sleep(1)
    linha()
escreva("CONTADOR DE NUMEROS")
print("Exemplo: ")
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez, escolha a sua contagem')
while True:
    inicio = int(input('Escolha o inicio: '))
    fim = int(input('Escolha o fim: '))
    check = True
    while check == True:
        passo = int(input('Escolha o passo: '))
        linha()
        if passo == 0:
            print('ERRO. O passo não pode ser 0.')
            check = True
        else:
            check = False
    contador(inicio, fim, passo)
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('-- Deseja continuar[S/N]: ')).strip().upper()[0]
        if pergunta not in 'SN':
            print('ERRO. Digite APENAS S ou N.')
            linha()
    if pergunta in 'N':
        print('Finalizando o programa...')
        sleep(1.5)
        break
linha()
print('Programa finalizado.')