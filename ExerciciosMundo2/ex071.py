print('='* 30)
print('        BANCO MILENIUM')
print('=' *30)
valor = int(input('Qual valor você quer sacar: R$ '))
cedulas200 = valor // 200
sob = valor % 200
cedulas100 = sob // 100
sobr = sob % 100
cedulas50 = sobr // 50
sobra = sobr % 50
cedulas20 = sobra // 20
sobra1 = sobra % 20
cedulas10 = sobra1 // 10
sobra2 = sobra1 % 10
cedulas1 = sobra2 // 1
print(f'{cedulas200} cedulas de 200')
print(f'{cedulas100} cedulas de 100')
print(f'{cedulas50} cedulas de 50')
print(f'{cedulas20} cedulas de 20')
print(f'{cedulas10} cedulas de 10')
print(f'{cedulas1} cedulas de 1')
print('=' *30)
print(f'Obrigado por escolher nosso Banco. Volte Sempre!')

#OUTRA MANEIRA DE FAZER:
#valor = int(input('Que valor você quer sacar? R$'))
#total = valor
#ced = 50
#totced = 0
#while True:
  #  if total >= ced:
 #       total -= ced
#       totced += 1
#    else:
#        totced > 0:
#        print(f'Total de {totced} cedulas de R${ced}')
#        if ced == 50:
#            ced = 20
#        elif ced == 20:
#            ced = 10
#        elif ced == 10:
#            ced = 1
#        totced = 0
#        if total == 0:
#            break
