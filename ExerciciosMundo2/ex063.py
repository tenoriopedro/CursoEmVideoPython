print('SEQUÊNCIA DE FIBONACCI')
print('*' *23)
termo = int(input('Digite quantos termos você quer mostrar: '))
penultimo = 0
ultimo = 1
print(f'{penultimo} -> {ultimo}', end=' -> ')
count = 3
while count <= termo:
    novo = penultimo + ultimo
    print(f'{novo}', end=' -> ')
    penultimo = ultimo
    ultimo = novo
    count += 1
print('FIM')
