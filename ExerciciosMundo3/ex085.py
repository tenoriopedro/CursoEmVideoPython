todos = [[], []]
for pos in range(0, 7):
    num = int(input(f'Digite o {pos+1}º valor: '))
    if num % 2 == 0:
        todos[0].append(num)
    else:
        todos[1].append(num)
todos[0].sort()
todos[1].sort()
print('-=' *30)
print(f'Os valores pares digitados foram: {todos[0]}')
print(f'Os valores impares digitados foram: {todos[1]}')