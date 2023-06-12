# .insert
numeros = []
        ### OUTRA MANEIRA ###
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > numeros[-1]:
        numeros.append(n)
        print('Adicionado ao final da lista')
    else:
         pos = 0
         while pos < len(numeros):
              if n <= numeros[pos]:
                  numeros.insert(pos, n)
                  print(f'Adicionado na posição {pos} da lista')
                  break
              pos += 1


#for contador in range(0, 5):
#    n = int(input('Digite um valor: '))
#
#    if contador == 0:
#        numeros.insert(0, n)
#        print('Valor foi adicionado ao final da lista.')
#    if contador == 1:
#        if n > numeros[0]:
#            numeros.insert(1, n)
#            print('Este valor é maior, por isso vai pro final da lista.')
#        if n < numeros[0]:
#            numeros.insert(0, n)
#            print('Este valor foi adicionado na posição 0.')
#    if contador == 2:
 #       if n < numeros[0] and n < numeros[1]:
 #           numeros.insert(0, n)
#            print('Este valor foi adicionado na posição 0.')
#        if n > numeros[0] and n > numeros[1]:
#            numeros.insert(2, n)
#            print('Este valor é o maior, por isso vai para o final da lista.')
#        if n > numeros[0] and n < numeros[1] or n < numeros[0] and n < numeros[1]:
#            numeros.insert(1, n)
#            print('Este valor foi adicionado na posição 1.')
#    if contador == 3:
#        if n > numeros[0] and n > numeros[1] and n > numeros[2]:
#            numeros.insert(3, n)
#            print('Este valor é ainda maior por isso vai pro final da lista.')
#        if n < numeros[0] and n < numeros[1] and n < numeros[2]:
#            numeros.insert(0, n)
#            print('Este valor foi adicionado na posição 0')
#        if n > numeros[0] and n < numeros[1] and n < numeros[2]:
#            numeros.insert(1, n)
#            print('Este valor foi adicionado na posição 1')
#        if n > numeros[0] and n > numeros[1] and n < numeros[2]:
#            numeros.insert(2, n)
#            print('Este valor foi adicionado na posição 2')
#    if contador == 4:
#        if n > numeros[0] and n > numeros[1] and n > numeros[2] and n > numeros[3]:
#            numeros.insert(4, n)
#            print('Este sim é o mair valor digitado até, portanto vai para o final da lista.')
#        if n < numeros[0] and n < numeros[1] and n < numeros[2] and n < numeros[3]:
#            numeros.insert(0, n)
#            print('Este valor foi adicionado na posição 0.')
#        if n > numeros[0] and n > numeros[1] and n > numeros[2] and n < numeros[3]:
#            numeros.insert(3, n)
#            print('Este valor foi adicionado na posição 3.')
#        if n > numeros[0] and n > numeros[1] and n < numeros[2] and n < numeros[3]:
#            numeros.insert(2, n)
#            print('Este valor foi adicionado na posição 2.')
#        if n > numeros[0] and n < numeros[1] and n < numeros[2] and n < numeros[3]:
#            numeros.insert(1, n)
#            print('Este valor foi adicionado na posição 1.')
print('-=' *40)
print(f'A lista que você digitou em ordem crescente: {numeros}')