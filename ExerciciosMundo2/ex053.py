print('*' *30)
print('   DETECTOR DE PALÍNDROMO')
print('*' *30)
frase = input('Digite uma frase: ').replace(' ', '').lower()
frase_inverso = ''
for c in range(len(frase) -1, -1, -1):
    frase_inverso += frase[c]
print(f'O inverso de {frase} é {frase_inverso}')
if frase_inverso == frase:
    print('Palindromo DETECTADO')
else:
    print('Palindromo NÃO DETECTADO')

#frase_inverso = frase[::-1]
#print(f'O inverso dessa frase é {frase_inverso}')
#if frase == frase_inverso:
#    print('Portando ela É um Palindromo')
#else:
#    print('Portando ela NAO é Palindromo')


