from random import randint
from time import sleep
pc = randint(0 ,5)
print('Vamos jogar o jogo da adivinhação\nVou pensar num numero de 0 a 5 e você terá que acertar')
numero = int(input('Digite aqui o número: '))
print('PROCESSANDO...')
sleep(3)
if numero == pc:
    print('PARABÉNS VOCÊ ACERTOU!!!!!\n Eu pensei no nº {} e você acertou'.format(pc))
else:
    print('Infelizmente você errou, eu pensei no nº{}'.format(pc))
