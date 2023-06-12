frase = str(input('Digite uma frase: ')).strip().upper()
print('Nessa frase a letra A aparece {} vezes'.format(frase.count('A')))
print('Primeira posição da letra A é {}'.format(frase.find('A')+1))
print('E a posição da ultima letra A é {}'.format(frase.rfind('A')+1))

