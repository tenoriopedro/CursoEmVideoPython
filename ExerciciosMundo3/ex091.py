from random import randint
from time import sleep
from operator import itemgetter  ### PARA POR DICIONÁRIO EM ORDEM CRESCENTE OU DECRESCENTE, USA-SE ESSA FUNÇÃO ###

jogo = {'jogador1': randint(1, 12),
        'jogador2': randint(1, 12),
        'jogador3': randint(1, 12),
        'jogador4': randint(1, 12)
        }
ranking = []
print('Valores sorteados:')
sleep(1)
for k, v in jogo.items():
    print(f'    O {k} tirou {v} nos dados')
    sleep(1)
print('=' *50)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) ## reverse=True para por em ordem decrescente ##
### key=itemgetter(x) -> para 0 = keys do dicionario // para 1 = values do dicionario ###
print(' == RANKING DOS JOGADORES ==')
sleep(1)
for p, j in enumerate(ranking):
    print(f'    {p+1}º lugar: {j[0]} com {j[1]} pontos.')
    sleep(1)