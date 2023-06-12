times = ('Benfica', 'Braga', 'Porto', 'Sporting', 'Casa Pia', 'Vitoria SC',
         'Arouca', 'Vizela', 'Chaves', 'Rio Ave', 'Portimonense', 'Boa Vista',
         'Famalicão', 'Estoril', 'Santa Clara', 'Gil Vicente', 'Maritimo', 'Paços de Ferreira')
print('TIMES DA LIGA PORTUGUESA')
print('=-' *30)
print(f'Os times são:\n{times}')
print('=-' *30)
print(f'Os CINCOS primeiros são:\n{times[:5]}')
print('=-' *30)
print(f'Os QUATRO ultimos são:\n{times[-4:]}')
print('=-' *30)
print(f'Times em ordem Alfabetica:\n{sorted(times)}')
print('=-' *30)
print(f'O time Casa Pia está em {times.index("Casa Pia")+1}º colocado')
