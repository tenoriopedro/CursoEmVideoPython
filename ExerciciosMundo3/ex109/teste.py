import moedas


p = float(input('Digite o preço: €'))
print(f'A metade de {moedas.moeda(p)} é {moedas.metade(p)}')
print(f'O dobro de {moedas.moeda(p)} é {moedas.dobro(p)}')
print(f'Aumentando 10% temos {moedas.aumentar(p, 10)}')
print(f'Reduzindo 14% temos {moedas.diminuir(p, 14)}')