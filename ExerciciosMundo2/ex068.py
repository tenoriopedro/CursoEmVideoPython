from random import randint
print('-=' *20)
print('      VAMOS JOGAR PAR OU IMPAR')
print('-=' *20)
count = 0
while True:
    #outra maneira de fazer
    #tipo = ' '
    pc = randint(0, 10)
    jogador = int(input('Escolha um numero: '))
    escolha = str(input('Escolha PAR ou IMPAR [P/I]: ')).strip().lower()[0]
    print('-' *20)
    resultado = pc + jogador
    #while tipo not in 'PpfF':
        #tipo = str(input('Par ou IMPAR [P/I]: ')).strip().lower()[0]
    print(f'Você jogou {jogador} e o PC jogou {pc} que será igual a {resultado}', end=' ')
    print('DEU PAR' if resultado % 2 == 0 else 'IMPAR')
    if escolha in 'p' and resultado % 2 == 0:
        print('VOCÊ VENCEU, vamos jogar novamente..')
        count += 1
    elif escolha in 'i' and resultado % 2 == 1:
        print('VOCÊ VENCEU, vamos jogar novamente..')
        count += 1
    else:
        print('VOCÊ PERDEU')
        break
if count == 0:
    print('GAME OVER!!! Você não venceu nenhuma.')
if count > 0:
    print(f'GAME OVER!!! Você conseguiu vencer {count} vezes.')