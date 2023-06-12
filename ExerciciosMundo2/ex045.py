from random import randint
from time import sleep
print('*=' *10)
print('      \033[1mJOKENPO\033[m')
print('*=' *10)
print('')
print('O computador lhe desafiou para uma partida de JOKENPO')
itens = ('Pedra', 'Papel','Tesoura')
computador = randint(0, 2)
print('''[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Escolha uma opção: '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
print('=-'* 15)
print('jogador escolheu {}'.format(itens[jogador]))
print('computador escolheu {} '.format(itens[computador]))
print('=-' * 15)
if jogador == 0 and computador == 0:
    print('EMPATE')
elif jogador == 1 and computador == 1:
    print('EMPATE')
elif jogador == 2 and computador == 2:
    print('EMPATE')
elif jogador == 0 and computador == 2:
    print('JOGADOR VENCEU')
elif jogador == 1 and computador == 0:
    print('JOGADOR VENCEU')
elif jogador == 2 and computador == 1:
    print('JOGADOR VENCEU')
elif jogador == 0 and computador == 1:
    print('COMPUTADOR VENCEU')
elif jogador == 1 and computador == 2:
    print('COMPUTADOR VENCEU')
elif  jogador == 2 and computador == 0:
    print('COMPUTADOR VENCEU')
else:
    print('OPÇÃO INVÁLIDA')