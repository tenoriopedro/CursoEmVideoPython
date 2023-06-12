dados = {}
dados['nome'] = str(input('Nome do aluno: '))
dados['media'] = float(input(f'Qual a média de {dados["nome"]}: '))
print('-' *20)
if dados['media'] >= 7.0:
    dados['situaçao'] = 'Aprovado'
else:
    dados['situaçao'] = 'Reprovado'
for k, v in dados.items():
    print(f'{k.title()}: {v:}')