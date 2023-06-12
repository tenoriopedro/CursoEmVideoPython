'''a + b < c
a + c < b
b + c < c'''
print('Me dê 3 retas e direi se podem ou não formarem um triângulo')
r1 = float(input('Reta nº1: '))
r2 = float(input('Reta nº2: '))
r3 = float(input('Reta nº3: '))
if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print('Essas retas PODEM formar um triangulo')
else:
    print('Essas retas NÃO PODEM formar um triangulo')

