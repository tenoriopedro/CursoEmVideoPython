print('=' *20)
print('\033[1;33mFORMAÇÃO DE TRIÂNGULOS\033[m')
print('=' *20)
print('')
print('Digite TRÊS retas e direi se podem ou não formar triangulo')
print('E também direi o TIPO de triângulo que pode formar')
r1 = float(input('1º reta: '))
r2 = float(input('2º reta: '))
r3 = float(input('3º reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Essas retas PODEM formar um triângulo.')
    print('Agora de acordo com essas retas')
    if r1 == r2 and r1 == r3 and r3 == r2: #OU pode fazer da seguinte forma: r1 == r2 == r3:
        print('Os três lados IGUAIS: EQUILÁTERO')
    elif r1 == r2 and r1 != r3 or r1 == r3 and r1 != r2 or r2 == r3 and r2 != r1:
        print('DOIS lados iguais e um DIFERENTE: ISOSCELES')
    elif r1 != r2 and r1 != r3 and r2 != r3: #OU pode fazer da seguinte forma r1 != r2 != r3 != r1:
        print('Os três lados DIFERENTES: ESCALENO')
else:
    print('Essas retas NÃO PODEM formar um triângulo.')
