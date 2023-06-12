print('\033[1;34m*' *40)
print('         GAZIL EQUIPAMENTOS')
print('*' *40, '\033[m')
soma = cont = cont_valor = 0
menor_valor = 0
nome_produto = ' '
while True:
    produto = str(input('Nome do produto: ')).strip()
    valor = float(input('Qual valor: R$'))
    cont_valor += 1
    soma += valor
    pergunta = ' '
    if valor >= 2000:
        cont += 1
    if cont_valor == 1:#or valor < menor_valor:
        menor_valor = valor
        nome_produto = produto
    if valor < menor_valor:
        menor_valor = valor
        nome_produto = produto
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if pergunta == 'N':
         break
print('---------------FIM DO PROGRAMA---------------')
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {cont} produtos custando mais de R$2000,00')
print(f'O produto mais barato foi {nome_produto}, que custa R${menor_valor:.2f}')