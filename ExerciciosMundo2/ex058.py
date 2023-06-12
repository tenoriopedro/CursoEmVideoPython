from random import randint
from time import sleep
print('*' *20)
print('JOGO DA ADIVINHAÇÃO')
print('*' *20)
sleep(1)
print('O PC pensará num numero de 0 a 10 e você terá que adivinha-lo.')
sleep(3)
print('E o jogo começa...')
sleep(2)
print('AGORA!!!!')
pc = randint(0, 10)
soma = 1
tentativa = int(input('Que numero o PC pensou? R: '))
if tentativa == pc:
    print('PARABÉEEEENS, VOCÊ ACERTOU DE PRIMEIRA.')
while pc != tentativa:
    if tentativa > pc:
        tentativa = int(input('É menos, Tente novamente: '))
        soma += 1
    if tentativa < pc:
        tentativa = int(input('É mais, tente novamente: '))
        soma += 1
    if tentativa == pc:
        if soma <= 4:
            print('VOCÊ ACERTOU!')
        if soma >= 5:
            print('UFA.. FINALMENTE, VOCÊ ACERTOU.')
print(f'O PC pensou no numero {pc} e você acertou digitando o numero {tentativa}')
print(f'Para acertar você precisou de {soma} tentativas.')

                        # OUTRA MANEIRA:
# acertou = False
# palpites = 0
# while not acertou:
#     jogador = int(input('Qual seu palpite? R: '))
#     palpites += 1
#     if jogador == pc:
#         acertou = True
#     else:
#         if jogador < computador:
#             print('Mais... Tente mais uma vez.')
#         elif jogador > computador:
#             print('Menos... Tente mais uma vez.')
# print(f'Acertou com {palpites} tentativas. Parabéns!')