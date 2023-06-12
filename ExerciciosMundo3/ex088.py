from random import randint
from time import sleep
print('-' *30)
print(f'{"MEGA SENA":^28}')
print('-' *30)

jogo = int(input('Você quer sortear quantos jogos? R: '))

numeros = []
jogos = []
tot = 1

while tot <= jogo:
    contador = 0

    while True:
        n = randint(1, 60)
        if n not in numeros:
            numeros.append(n)
            contador += 1
        if contador == 6:
            break

    numeros.sort()
    jogos.append(numeros[:])
    numeros.clear()
    tot += 1

for j, jogo in enumerate(jogos):
    print(f'Jogo {j+1} : {jogo}')
    sleep(1)