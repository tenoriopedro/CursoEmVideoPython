print('*' *20)
print('PROGRESSÃO ARITMÉTICA')
print('*' *20)
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro_termo
count = 1
while count <= 10:
    print(f'{termo}', end=' -> ')
    termo += razao
    count += 1
print('FIM')