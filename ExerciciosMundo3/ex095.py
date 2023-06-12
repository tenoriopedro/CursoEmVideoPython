from time import sleep
jogadores = []
jogador = {}
quant_gols = []
while True:
    jogador['nome'] = str(input('Nome do jogador: ')).title().strip()
    check = True
    while check == True:
        partidas = input(f'Quantas partidas {jogador["nome"]} jogou: ')
        if partidas.isnumeric() == True:
            check = False
        else:
            print('ERRO! Por Favor digite apenas números.')
            check = True
    partidas = int(partidas)
    cont = 0

    jogador['gols'] = 0
    jogador['total'] = 0
    while cont < partidas:
        quant_gols.append(int(input(f'    Quantos gols na {cont+1}ª partida: ')))
        cont += 1
        jogador['gols'] = quant_gols[:]
        jogador['total'] = sum(quant_gols)
    jogadores.append(jogador.copy())
    quant_gols.clear()
    pergunta = ' '
    while pergunta not in 'sn':
        pergunta = str(input('Quer continuar[S/N]: ')).lower().strip()[0]
        if pergunta not in 'sn':
            print('ERRO! Por favor digite S ou N.')
    if pergunta == 'n':
        break
    print('-=' *30)
#print('-=' *30)
print(f'{"Nº":<4}{"NOME":<10}{"GOLS":>8}    {"TOTAL":>10}')

for j, p in enumerate(jogadores):
    print(f'{j+1:<4}{str(p["nome"]):<10}{str(p["gols"]):>10}   {str(p["total"]):>8}')
while True:
    print('-=' *30)
    resposta = 0
    while resposta != 999:
        check = True
        while check == True:
            resposta = input('Mostrar dados de qual jogador (999 STOP): ')
            if resposta.isnumeric() == True:
                check = False
            else:
                print('ERRO. Por favor digite apenas numeros.')
                check = True
        resposta = int(resposta)
        if resposta <= 0 or resposta > len(jogadores) and resposta != 999:
            print('Numero errado, tente novamente. Não existe jogador com esse numero.')
            print('-=' *30)
        if resposta <= len(jogadores) and resposta > 0:
            print(f'--LEVANTAMENTO DO JOGADOR {jogadores[resposta-1]["nome"]}:')
            for j, item in enumerate(jogadores[resposta-1]['gols']):
                print(f'    No jogo {j+1} fez {item} gols')
            print('-=' * 30)
    if resposta == 999:
        print('Finalizando...')
        break

sleep(1.5)
print('PROGRAMA FINALIZADO')
