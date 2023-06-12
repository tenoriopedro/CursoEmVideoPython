fim = False
soma = 0
count = 0
while not fim:
    num = int(input('Digite um número (para parar digite 999): '))
    if num == 999:
        fim = True
    else:
        count += 1
        soma += num
print(f'Você digitou {count} números e a soma entre eles é {soma}')