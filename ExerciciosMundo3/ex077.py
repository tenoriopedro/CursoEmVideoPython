palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'praticar', 'estudar',
            'trabalhar', 'mercado', 'programar', 'futuro')
#palavra = palavras[0]
#print(palavra[0])
for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos',end=' ')
    for vogal in palavra:
        if vogal.lower() in 'aeiou':
            print(f'{vogal}',end=' ')
        #if vogal == 'a' or vogal == 'e' or vogal == 'i' or vogal == 'o' or vogal == 'u':

           # print(f'{vogal}', end=' ')
        #if v == 'e':
            #print(v)
        #if v == 'i':
            #print(v)
        #if v == 'o':
            #print(v)
        #if v == 'u':
            #print(v)

