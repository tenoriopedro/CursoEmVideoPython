print('=' *20)
print(' \033[1;34mGAZIL EQUIPAMENTOS\033[m')
print('=' *20)
valor_produto = float(input('Qual valor TOTAL da compra: '))
pagamento = str(input('Qual a forma de pagamento: ')).lower()
if pagamento == 'cheque' or pagamento == 'a vista':
    print('Pagamentos nessa modalidade ganha um desconto de 10%')
    print('Portanto de {:.2f}€ o cliente poderá pagar {:.2f}€.'.format(valor_produto, valor_produto *(1 - 0.10)))
elif pagamento == 'cartao a vista':
    print('Pagamentos nessa modalidade ganha um desconto de 5%')
    print('Portanto de {:.2f}€ o cliente poderá pagar {:.2f}€'.format(valor_produto, valor_produto *(1 - 0.05)))
elif pagamento == '2x no cartao':
    print('Valor sem descontos')
    print('O cliente pagará o valor {:.2f} em duas parcelas de {:.2f}'.format(valor_produto, valor_produto / 2))
elif pagamento == '3x ou mais no cartao':
    print('Pagamentos nessa modalidade acrescenta um juros de 20%')
    parcelas = int(input('Em quantas parcelas o cliente quer pagar: '))
    valor_parcelas = valor_produto / parcelas * (1 + 0.20)
    print('A compra será parcelada em {}x com JUROS de 20%'.format(parcelas))
    print('O valor das parcelas será de {:.2f}€'.format(valor_parcelas))
else:
    print('OPÇÃO INVALIDA')
