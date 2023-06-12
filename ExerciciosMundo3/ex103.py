def ficha(nome='<desconhecido>', gols=0):

    print(f'O jogador {nome} fez {gols} gol(s) no campeonato ')


nome = str(input('Nome do jogador: ')).strip()
gols = input(f'Numero de gols: ').strip()
if nome == '' and gols == '':
    gols = 0
    ficha(gols=gols)
if gols.isnumeric() == False:
    ficha(nome=nome)
elif nome.isalpha() == True:
    ficha(nome=nome,gols=gols)
else:
    ficha(gols=gols)
