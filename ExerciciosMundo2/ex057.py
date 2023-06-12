check = ''
while check != 'ok':
    sexo = str(input('Qual seu sexo [M/F]: ')).strip().upper()
    if sexo not in 'MF':
        check = 'error'
        print('Digite novamente ')
    else:
        if sexo in 'MF':
            check = 'ok'
print(f'O sexo {sexo}, foi lido com sucesso')

#sexo = ''
#while sexo != 'M' and sexo != 'F':
    #sexo = str(input('Qual seu sexo [M/F]: ')).upper().strip()[0]
    #if sexo == 'M':
     #   print('Você é uma pessoa do sexo MASCULINO')
    #if sexo == 'F':
   #     print('Você é uma pessoa do sexo FEMININO')
  #  else:
 #       if sexo != 'M' and sexo != 'F':
#            print('\033[1;31mOPÇÃO INVALIDA\033[m, digite novamente')

            #OUTRA MANEIRA...
#sexo = str(input('Qual seu sexo [M/F]: ')).strip().upper()[0]
#while sexo not in 'MmFf':
   # sexo = str(input('Opção invalida, digite novamente: ')).upper().strip()[0]
#print(f'Sexo {sexo} lido com sucesso')'''
