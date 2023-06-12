dados = {}
dados['jogador'] = str(input('Nome do jogador: ')).title().strip()
partidas = int(input(f'Quantas partidas {dados["jogador"]} jogou: '))
cont = 0
quant_gols = []
dados['total'] = 0
while cont < partidas:
    quant = int(input(f'    Quantos gols na {cont+1}ª partida: '))
    quant_gols.append(quant)
    cont += 1
    dados['gols'] = quant_gols
    dados['total'] += quant

print('=-' *30)
print(dados)

print('=-' *30)
for k, v in dados.items():
    print(f'O campo {k} tem valor {v}')
print('=-' *30)
print(f'O jogador {dados["jogador"]}, jogou {partidas} partidas')

for jg, gol in enumerate(dados['gols']):
    print(f'   => Na {jg+1}ª partida {dados["jogador"]}, fez {gol} gols')
print(f'Foi um total de {dados["total"]} gols de {dados["jogador"]}.')