s = 0
cont = 0
for c in range(0, 500, 3):
    if c % 2 == 1:
        cont += 1
        s += c
print(f'A soma dos {cont} numeros que são IMPARES e multiplos de TRES são {s}')
