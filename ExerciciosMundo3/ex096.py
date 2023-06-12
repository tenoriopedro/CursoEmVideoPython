# A = a * b
def area(a, b):
    a2 = a * b
    print(f'De acordo com os dados passados, a área desse terreno é de {a2:.2f}m2.')

def linha():
    print('~' *30)

linha()
print('     Controle de Terreno')
linha()
a = float(input('Digite a largura do terreno (m): '))
b = float(input('Digite o comprimento do terreno (m): '))
linha()
area(a, b)