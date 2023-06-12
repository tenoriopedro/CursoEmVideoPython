a = input('Digite algo: ')
print('O tipo primitivo desse valor é: ', type(a))
print('{} é decimal?'.format(a), a.isdecimal())
print('{} é um numero?'.format(a), a.isnumeric())
print('{} é capitalizado?'.format(a), a.istitle())
print('{} é alfanumerico?'.format(a), a.isalnum())
print('{} é alfabetico?'.format(a), a.isalpha())

