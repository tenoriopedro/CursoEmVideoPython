## se aposenta com 35 anos de colaboração ##
from datetime import date
ano_atual = date.today().year
dados = {}
dados['nome'] = str(input('Nome: ')).strip().title()
ano_nascimento = int(input('Ano de nascimento: '))
dados['idade'] = ano_atual - ano_nascimento
dados['ctps'] = int(input('Carteira de Trabalho, (0 = não tem): '))
if dados['ctps'] != 0:
    dados['contrato'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Qual salário: €'))
    dados['aposentadoria'] = (dados['contrato'] + 35) - ano_nascimento
    print('=-' *20)
    for k, v in dados.items():
        print(f'{k.title()}, tem valor: {v}')
else:
    print('=-' *20)
    for k, v in dados.items():
        print(f'{k.title()}, tem valor: {v}')
