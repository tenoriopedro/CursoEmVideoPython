import moedas


p = float(input('Digite o preço: €'))
print(f'A metade de {moedas.moeda(p)} é {moedas.metade(p, True)}')
#print(f'O dobro de {moedas.moedas(p)} é {moedas.moedas(moedas.dobro(p))}')
#print(f'Aumentando 10%, temos {moedas.moedas(moedas.aumentar(p, 10))}')