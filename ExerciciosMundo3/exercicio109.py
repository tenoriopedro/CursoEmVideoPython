from ex109 import moedas

p = float(input('Digite o preço: €'))
print(f'A metade de {moedas.moeda(p)} é {moedas.metade(p, True)}')
print(f'O dobro de {moedas.moeda(p)} é {moedas.dobro(p, True)}')
print(f'Aumentando 10% temos {moedas.aumentar(p, 10, True)}')
print(f'Reduzindo 14% temos {moedas.diminuir(p, 14, True)}')